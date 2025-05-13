import pytest
from playwright.sync_api import sync_playwright, Browser, BrowserContext, Page
import allure

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

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Получаем результат выполнения теста
    outcome = yield
    result = outcome.get_result()

    # Доступ к page через фикстуру, если она есть
    if result.when == "call" and result.failed:
        page = item.funcargs.get("page", None)
        if page:
            allure.attach(
                page.screenshot(full_page=True),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG
            )
            allure.attach(
                page.content(),
                name="page source",
                attachment_type=allure.attachment_type.HTML
            )