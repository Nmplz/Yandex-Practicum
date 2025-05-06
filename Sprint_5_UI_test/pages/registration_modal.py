import allure
from pages.base_page import BasePage
from pages.locators import RegistrationFormLocators, BasePageLocators
from utils.generators import generate_random_email, generate_randon_password


class RegistrationModal(BasePage):

    @allure.step("Переход во вкладку 'Нет аккаунта?'")
    def go_to_no_account_menu(self):
        self.click(RegistrationFormLocators.NO_ACCOUNT_BUTTON)

    @allure.step("Вводим email нового пользователя")
    def enter_new_user_email(self, domain: str = "@mail.ru"):
        email = generate_random_email(domain)
        link = self.wait_for_clickable(RegistrationFormLocators.ENTER_EMAIL)
        link.send_keys(email)

    @allure.step("Вводим email существующего пользователя: {email}")
    def enter_existing_email(self, email):
        link = self.wait_for_clickable(RegistrationFormLocators.ENTER_EMAIL)
        link.send_keys(email)

    @allure.step("Вводим пароль для нового пользователя (и повторно)")
    def enter_new_user_password(self):
        password = generate_randon_password()

        pwd_field = self.find(RegistrationFormLocators.ENTER_PASSWORD)
        pwd_field.send_keys(password)
        pwd_field_2 = self.find(RegistrationFormLocators.ENTER_PASSWORD_REPITE)
        pwd_field_2.send_keys(password)

    @allure.step("Вводим пароль для авторизации")
    def enter_existing_user_password(self, password):
        pwd_field = self.find(RegistrationFormLocators.ENTER_PASSWORD)
        pwd_field.send_keys(password)

    @allure.step("Отправляем форму регистрации")
    def submit_account_creation(self):
        link = self.click(RegistrationFormLocators.CREATE_ACCOUNT_BUTTON)

    @allure.step("Проверяем, отображается ли ошибка email")
    def is_email_error_displayed(self):
        error_text = self.wait_for_clickable(RegistrationFormLocators.ERROR_MESSAGE)
        return error_text.is_displayed()

    @allure.step("Проверяем цвет рамки у поля с ошибкой")
    def is_errored_fields_highlighted_red(self):
        wrapper = self.find(RegistrationFormLocators.ERROR_RED_BOX)
        return wrapper.value_of_css_property("border-color")

    @allure.step("Проверяем, что появилось предупреждающее модальное окно")
    def is_modal_with_warring_displayed(self):
        result = self.is_element_with_text_present(*BasePageLocators.WARNING_AUTHORISATION_MODAL_WINDOW, "Чтобы разместить объявление, авторизуйтесь")
        return result

    @allure.step("Отправляем форму входа")
    def submit_login_form_button(self):
        self.click(RegistrationFormLocators.LOGIN_FORM_ENTER_BUTTON)

    @allure.step("Выходим из аккаунта")
    def submit_logout_button(self):
        self.click(RegistrationFormLocators.LOGIN_FORM_LOGOUT_BUTTON)
