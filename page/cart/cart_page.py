from page.base_page import BasePage
from page.cart.cart_locators import *
from page.cart.cart_data import *
from page.inventory.inventory_locators import *

class CartPage(BasePage):
    def remove_products_from_cart(self):
        self.click(REMOVE_FROM_CART_1)
        self.click(REMOVE_FROM_CART_2)

    def checkout_go_to_pay(self):
        self.click(CHECKOUT_BUTTON)