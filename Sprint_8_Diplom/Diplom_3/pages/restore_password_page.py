import allure

from locators.restore_password_page_locators import RestorePasswordPageLocators
from pages.base_page import BasePage
from utils.generators import generate_email


class RestorePasswordPage(BasePage):

    @allure.step("Ввод email и подтверждение восстановления пароля")
    def enter_email_and_confirm(self):
        self.click(RestorePasswordPageLocators.EMAIL_FIELD)
        self.send_keys(RestorePasswordPageLocators.EMAIL_FIELD, generate_email())
        self.click(RestorePasswordPageLocators.RESTORE_PASSWORD_BUTTON)
        self.wait_for_presence(RestorePasswordPageLocators.NEW_PASSWORD_CONFIRM_BUTTON)

    @allure.step("Нажатие на иконку отображения пароля")
    def click_shows_password_icon(self):
        self.click_on_element(RestorePasswordPageLocators.SHOW_PASSWORD_TOGGLE)

    @allure.step("Проверка, что поле пароля активно")
    def check_is_password_field_active(self):
        return self.check_displaying_of_element(RestorePasswordPageLocators.PASSWORD_FIELD_IS_ACTIVE)
