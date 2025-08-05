import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @allure.step("Нажатие кнопки «Войти в аккаунт»")
    def press_login_button(self):
        self.click(MainPageLocators.LOGIN_BUTTON)

    @allure.step("Нажатие кнопки «Войти в Личный кабинет»")
    def press_profile_button(self):
        self.forse_click(MainPageLocators.PROFILE_BUTTON)

    @allure.step("Вход в личный кабинет после авторизации")
    def go_to_profile_after_auth(self):
        self.forse_click(MainPageLocators.PROFILE_BUTTON)

    @allure.step("Переход по кнопке Конструктор")
    def go_to_constructor_button(self):
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Переход по кнопке Лента Заказов")
    def go_to_orders_feed_button(self):
        self.forse_click(MainPageLocators.ORDER_FEED_BUTTON)
