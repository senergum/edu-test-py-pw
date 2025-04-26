# конфиг файл запуска браузера playwright
import pytest
from playwright.sync_api import sync_playwright, Browser, BrowserContext, Page

# Конфигурация через pytest (CLI или pytest.ini)
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox", choices=["chromium", "firefox", "webkit"], help="Выбор браузера")
    parser.addoption("--headless", action="store_true", help="Пуск браузера в скрытом режиме")

@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(request, playwright):
    browser_type = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    browser = getattr(playwright, browser_type).launch(headless=headless, slow_mo=1000)
    yield browser
    browser.close()

@pytest.fixture
def context(browser):
    context = browser.new_context(viewport={"width": 1280, "height": 720})
    yield context
    context.close()

@pytest.fixture
def page(context):
    page = context.new_page()
    yield page
    page.close()