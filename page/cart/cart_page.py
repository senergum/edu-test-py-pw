from page.base_page import BasePage
from config.utils.actions import ActionPage
from config.utils.asserts import AssertPage
from page.cart.cart_locators import *
from page.cart.cart_data import *
from page.inventory.inventory_locators import *


class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.actions = ActionPage(page)
        self.asserts = AssertPage(page)

    def remove_products_from_cart(self):
        self.actions.click(REMOVE_FROM_CART_1)
        self.actions.click(REMOVE_FROM_CART_2)

    def checkout_go_to_pay(self):
        self.actions.click(CHECKOUT_BUTTON)
