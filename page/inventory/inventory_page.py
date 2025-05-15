from playwright.sync_api import expect
from page.base_page import BasePage
from config.utils.actions import ActionPage
from config.utils.asserts import AssertPage
from page.inventory.inventory_locators import *
from page.inventory.inventory_data import *


class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.actions = ActionPage(page)
        self.asserts = AssertPage(page)

    def sort_products_low_to_high(self):
        self.actions.select_option(SORT_DROPDOWN, SORT_OPTION_VALUE)

    def add_products(self):
        self.actions.click(ADD_TO_CART_1)
        self.actions.click(ADD_TO_CART_2)

    def remove_products(self):
        self.actions.click(REMOVE_FROM_CART_1)
        self.actions.click(REMOVE_FROM_CART_2)

    @property
    def cart_badge(self):
        return self.page.locator(SHOPPING_CART_BADGE)

    def cart_badge_value(self, value):
        expect(self.cart_badge).to_have_text(str(value))

    def cart_badge_not_visible(self):
        expect(self.cart_badge).not_to_be_visible()

    def go_to_cart(self):
        self.actions.click(SHOPPING_CART)
