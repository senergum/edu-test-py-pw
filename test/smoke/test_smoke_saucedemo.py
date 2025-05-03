import pytest
from page.login.login_page import LoginPage
from page.login.login_data import *
from page.inventory.inventory_page import InventoryPage
from page.inventory.inventory_data import *
from page.cart.cart_page import CartPage
from page.cart.cart_data import *
from page.pay.pay_page import PayPage
from page.pay.pay_data import *

# Шаблон тестовой фикстуры
"""
@pytest.fixture
def имя_метода(page):
    return КЛАСС_МЕТОДА(page)
"""
# Шаблон тестового метода
"""
class TestSauceDemo:
    @pytest.mark.smoke
    def test_имя_метода(self, имя_метода):
        шаги тестов:
        модель_теста.метод_теста
"""

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
def pay_page(page):
    return PayPage(page)

@pytest.fixture
def logged_in_page(login_page):
    login_page.login()
    yield login_page.page
    login_page.logout()

class TestSauceDemo:
    @pytest.mark.smoke
    def test_login_logout(self, login_page):
        """Проверка входа и выхода"""
        login_page.login()
        assert login_page.page.url == INVENTORY_URL
        login_page.logout()
        assert login_page.page.url == LOGIN_URL

    @pytest.mark.smoke
    def test_product_sorting(self, logged_in_page, inventory_page):
        """Проверка сортировки товаров"""
        inventory_page.sort_products_low_to_high()
        # Здесь можно добавить проверку корректности сортировки

    @pytest.mark.smoke
    def test_add_to_cart(self, logged_in_page, inventory_page):
        """Добавление товаров в корзину"""
        inventory_page.add_products()
        # Проверка увеличения счетчика корзины
        inventory_page.cart_badge_value(2)
        # Удаление продуктов
        inventory_page.remove_products()
        # Проверка отсутствия счетчика корзины
        inventory_page.cart_badge_not_visible()

    @pytest.mark.smoke
    def test_cart(self, logged_in_page, cart_page, inventory_page):
        """Добавление товаров в корзину"""
        inventory_page.add_products()
        inventory_page.go_to_cart()
        # Проверка содержимого корзины

        # Очистка корзины
        cart_page.remove_products_from_cart()
        # Проверка очистки корзины


    @pytest.mark.smoke
    def test_checkout_flow(self, logged_in_page, inventory_page, cart_page, pay_page):
        """Оформление заказа"""
        # Шаг 1: Добавление товаров
        inventory_page.add_products()
        inventory_page.go_to_cart()
        # Шаг 2: Оформление
        cart_page.checkout_go_to_pay()
        pay_page.fill_checkout_info()
        pay_page.finish_checkout()
        # Проверка успешного оформления
        assert "complete" in pay_page.page.url
        # Проверка очистки корзины


    @pytest.mark.smokefull
    def test_full_flow(self, login_page, inventory_page, cart_page, pay_page):
        """Полный smoke-тест основного потока"""
        # Логин
        login_page.login()
        # Сортировка и добавление товаров
        inventory_page.sort_products_low_to_high()
        inventory_page.add_products()
        inventory_page.go_to_cart()
        # Оформление заказа
        cart_page.checkout_go_to_pay()
        pay_page.fill_checkout_info()
        pay_page.finish_checkout()
        # Проверки
        assert login_page.page.url == PAY_URL
        # Выход
        login_page.logout()
        assert login_page.page.url == LOGIN_URL