from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

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