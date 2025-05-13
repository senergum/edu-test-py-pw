from playwright.sync_api import Page
from config.logger import get_logger

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = get_logger(self.__class__.__name__)

    def navigate(self, url):
        self.page.goto(url)

    def click(self, locator):
        self.page.click(locator)

    def fill(self, locator, text):
        self.page.fill(locator, text)

    def select_option(self, locator, value):
        self.page.select_option(locator, value=value)

    def wait_for_url(self, url):
        self.page.wait_for_url(url)