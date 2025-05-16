import pytest
import allure
import os
from playwright.sync_api import sync_playwright, Browser, BrowserContext, Page


# Конфигурация для обработки параметров через pytest
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox", choices=["chromium", "firefox", "webkit"], help="Выбор браузера")
    parser.addoption("--headless", action="store_true", help="Запуск браузера в скрытом режиме")

# Фикстура для playwright
@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p

# Фикстура для браузера, выбираем браузер и headless через параметры
@pytest.fixture(scope="session")
def browser(request, playwright):
    browser_name = request.config.getoption("--browser", default="chromium")  # Получаем браузер (по умолчанию chromium)
    headless = request.config.getoption("--headless", default=False)  # Получаем headless (по умолчанию False)
    browser = getattr(playwright, browser_name).launch(headless=headless)
    yield browser
    browser.close()

# Фикстура для контекста
@pytest.fixture
def context(browser):
    context = browser.new_context(viewport={"width": 1280, "height": 720})
    yield context
    context.close()

# Фикстура для страницы
@pytest.fixture
def page(context):
    page = context.new_page()
    yield page
    page.close()

# Хук для создания скриншота
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    # Делаем только на шаге выполнения теста
    if result.when != "call":
        return

    # Достаём объект page, если он есть
    page = item.funcargs.get("page", None)
    if not page:
        return

    # Подготовка пути к скриншоту
    screenshots_dir = os.path.join("reports", "screenshots")
    os.makedirs(screenshots_dir, exist_ok=True)

    # Генерация имени файла на основе имени теста
    safe_test_name = item.nodeid.replace("/", "_").replace("::", "__").replace(" ", "_")
    screenshot_path = os.path.join(screenshots_dir, f"{safe_test_name}.png")

    try:
        # Сохраняем скриншот
        page.screenshot(path=screenshot_path, full_page=True)

        # Передаём в аллюр
        allure.attach.file(
            screenshot_path,
            name=f"Screenshot - {item.name}",
            attachment_type=allure.attachment_type.PNG
        )

        # Также прикрепим исходный код страницы
        html_path = os.path.join(screenshots_dir, f"{safe_test_name}.html")
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(page.content())
        allure.attach.file(
            html_path,
            name=f"Page Source - {item.name}",
            attachment_type=allure.attachment_type.HTML
        )

    except Exception as e:
        print(f"❌ Ошибка при создании или прикреплении скриншота: {e}")