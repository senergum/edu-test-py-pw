import allure
from page.base_page import BasePage
from config.utils.actions import ActionPage
from config.utils.asserts import AssertPage
from page.login.login_locators import *
from page.login.login_data import *


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.actions = ActionPage(page)
        self.asserts = AssertPage(page)

    @allure.step(f"Логинимся под пользователем: {STANDARD_USER}")
    def login(self, username=STANDARD_USER, password=PASSWORD):
        self.actions.logger.info(f"Логинимся учёткой: {username}")
        self.actions.navigate(LOGIN_URL)
        # Проверяем, что форма логина видима
        self.asserts.element_is_visible(USERNAME_INPUT)
        self.asserts.element_is_visible(PASSWORD_INPUT)
        self.asserts.element_is_visible(LOGIN_BUTTON)
        # Заполняем поля и логинимся
        self.actions.fill(USERNAME_INPUT, username)
        self.actions.fill(PASSWORD_INPUT, password)
        self.actions.click(LOGIN_BUTTON)
        # Проверяем, что авторизация удалась
        self.actions.wait_for_url(f"{LOGIN_URL}inventory.html")
        self.asserts.url_is(f"{LOGIN_URL}inventory.html")

    @allure.step(f"Логинимся под пользователем: {ERROR_USER}")
    def login_error(self, username=ERROR_USER, password=PASSWORD):
        self.actions.logger.info(f"Пробуем залогиниться с ошибочной учёткой: {username}")
        self.actions.navigate(LOGIN_URL)
        # Проверяем, что форма логина видима
        self.asserts.element_is_visible(USERNAME_INPUT)
        self.asserts.element_is_visible(PASSWORD_INPUT)
        self.asserts.element_is_visible(LOGIN_BUTTON)
        # Заполняем поля и логинимся
        self.actions.fill(USERNAME_INPUT, username)
        self.actions.fill(PASSWORD_INPUT, password)
        self.actions.click(LOGIN_BUTTON)
        # Проверяем, что остались на странице логина (т.е. ошибка)
        self.asserts.url_is(LOGIN_URL)
        # Дополнительно: можно проверить наличие сообщения об ошибке
        self.asserts.element_is_visible(ERROR_MESSAGE)

    @allure.step("Выход из системы")
    def logout(self):
        self.actions.logger.info("Выход из системы")
        self.actions.click(MENU_BUTTON)
        self.asserts.element_is_visible(LOGOUT_BUTTON)
        self.actions.click(LOGOUT_BUTTON)

        self.actions.wait_for_url(LOGIN_URL)
        self.asserts.url_is(LOGIN_URL)