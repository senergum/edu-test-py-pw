from page.base_page import BasePage
from page.inventory.inventory_locators import *
from page.inventory.inventory_data import *

class InventoryPage(BasePage):
    def sort_products_low_to_high(self):
        self.select_option(SORT_DROPDOWN, SORT_OPTION_VALUE)

    def add_products_to_cart(self):
        self.click(ADD_TO_CART_1)
        self.click(ADD_TO_CART_2)

    def go_to_cart(self):
        self.click(SHOPPING_CART)