import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step("Переход по линку восстановления пароля")
    def go_to_restore_password_link(self):
        self.click(LoginPageLocators.RESTORE_PASSWORD_LINK)

    @allure.step("Авторизация пользователя на сайте")
    def login_in_profile(self, email, password):
        self.send_keys(LoginPageLocators.EMAIL_FIELD, email)
        self.send_keys(LoginPageLocators.PASSWORD_FIELD, password)
        self.forse_click(LoginPageLocators.ENTER_BUTTON)
        self.wait_for_invisibility(LoginPageLocators.ENTER_BUTTON)
