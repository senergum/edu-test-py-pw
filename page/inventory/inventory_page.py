from playwright.sync_api import expect
from page.base_page import BasePage
from page.inventory.inventory_locators import *
from page.inventory.inventory_data import *

class InventoryPage(BasePage):
    def sort_products_low_to_high(self):
        self.select_option(SORT_DROPDOWN, SORT_OPTION_VALUE)

    def add_products(self):
        self.click(ADD_TO_CART_1)
        self.click(ADD_TO_CART_2)

    def remove_products(self):
        self.click(REMOVE_FROM_CART_1)
        self.click(REMOVE_FROM_CART_2)

    @property
    def cart_badge(self):
        return self.page.locator(SHOPPING_CART_BADGE)

    def cart_badge_value(self, value):
        expect(self.cart_badge).to_have_text(str(value))

    def cart_badge_not_visible(self):
        expect(self.cart_badge).not_to_be_visible()

    def go_to_cart(self):
        self.click(SHOPPING_CART)