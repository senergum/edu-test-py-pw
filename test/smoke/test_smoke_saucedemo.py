import pytest
from page.login.login_page import LoginPage
from page.login.login_data import *
from page.inventory.inventory_page import InventoryPage
from page.inventory.inventory_data import *
from page.cart.cart_page import CartPage
from page.cart.cart_data import *

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def inventory_page(page):
    return InventoryPage(page)

@pytest.fixture
def cart_page(page):
    return CartPage(page)

@pytest.fixture
def logged_in_page(login_page):
    login_page.login()
    yield login_page.page
    login_page.logout()

class TestSauceDemo:
    @pytest.mark.smoke
    def test_login_logout(self, login_page):
        """Smoke test: проверка входа и выхода"""
        login_page.login()
        assert login_page.page.url == INVENTORY_URL
        login_page.logout()
        assert login_page.page.url == LOGIN_URL

    @pytest.mark.smoke
    def test_product_sorting(self, logged_in_page, inventory_page):
        """Smoke test: проверка сортировки товаров"""
        inventory_page.sort_products_low_to_high()
        # Здесь можно добавить проверку корректности сортировки

    @pytest.mark.smoke
    def test_add_to_cart(self, logged_in_page, inventory_page):
        """Добавление товаров в корзину"""
        inventory_page.add_products_to_cart()
        # Можно добавить проверку счетчика корзины

    @pytest.mark.smoke
    def test_checkout_flow(self, logged_in_page, inventory_page, cart_page):
        """Полный поток оформления заказа"""
        # Шаг 1: Добавление товаров
        inventory_page.add_products_to_cart()
        inventory_page.go_to_cart()
        # Шаг 2: Оформление
        cart_page.checkout()
        cart_page.fill_checkout_info()
        cart_page.finish_checkout()
        # Проверка успешного оформления
        assert "complete" in cart_page.page.url

    @pytest.mark.smokefull
    def test_full_flow(self, login_page, inventory_page, cart_page):
        """Полный smoke-тест основного потока"""
        # Логин
        login_page.login()
        # Сортировка и добавление товаров
        inventory_page.sort_products_low_to_high()
        inventory_page.add_products_to_cart()
        inventory_page.go_to_cart()
        # Оформление заказа
        cart_page.checkout()
        cart_page.fill_checkout_info()
        cart_page.finish_checkout()
        # Проверки
        assert "complete" in cart_page.page.url
        assert login_page.page.url == CART_URL
        # Выход
        login_page.logout()
        assert login_page.page.url == LOGIN_URL