from page.base_page import BasePage
from config.utils.actions import ActionPage
from config.utils.asserts import AssertPage
from page.pay.pay_data import *
from page.pay.pay_locators import *


class PayPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.actions = ActionPage(page)
        self.asserts = AssertPage(page)

    def fill_checkout_info(self):
        self.actions.fill(FIRST_NAME_INPUT, FIRST_NAME)
        self.actions.fill(LAST_NAME_INPUT, LAST_NAME)
        self.actions.fill(POSTAL_CODE_INPUT, ZIP_CODE)
        self.actions.click(CONTINUE_BUTTON)

    def finish_checkout(self):
        self.actions.click(FINISH_BUTTON)
