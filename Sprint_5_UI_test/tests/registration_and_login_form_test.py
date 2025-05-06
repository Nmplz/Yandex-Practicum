import pytest
import allure
from pages.main_page import MainPage
from pages.registration_modal import RegistrationModal
from data import TestCredentials


class TestRegistrationAndLoginForm:

    @allure.title("Успешная регистрация нового пользователя")
    @pytest.mark.registration_form
    def test_user_registration_true(self, browser):

        page = MainPage(browser)
        page.open()
        page.go_to_enter_and_registration_form()

        form = RegistrationModal(browser)
        form.go_to_no_account_menu()
        form.enter_new_user_email()
        form.enter_new_user_password()
        form.submit_account_creation()

        assert page.is_current_url_correct(suffix="regiatration"), "Неверный URL после регистрации"
        assert page.is_user_avatar_displayed(), "Аватар не отображается"
        assert page.is_user_name_displayed(), "Имя пользователя не отображается"

    @allure.title("Ошибка при регистрации с некорректным email")
    @pytest.mark.registration_form
    def test_user_registration_invalid_email_false(self, browser):

        page = MainPage(browser)
        page.open()
        page.go_to_enter_and_registration_form()

        form = RegistrationModal(browser)
        form.go_to_no_account_menu()
        form.enter_new_user_email("mail.ru")
        form.enter_new_user_password()
        form.submit_account_creation()

        assert form.is_email_error_displayed(), "Нет сообщения 'Ошибка' под email"
        assert form.is_errored_fields_highlighted_red() == "rgb(255, 105, 114)", "Ожидался красный цвет границы при ошибке"

    @allure.title("Ошибка при попытке зарегистрировать уже существующего пользователя")
    @pytest.mark.user_login
    def test_registration_existing_user_fails(self, browser):

        page = MainPage(browser)
        page.open()
        page.go_to_enter_and_registration_form()

        form = RegistrationModal(browser)
        form.go_to_no_account_menu()
        form.enter_existing_email(TestCredentials.EMAIL)
        form.enter_new_user_password()
        form.submit_account_creation()

        assert form.is_email_error_displayed(), "Нет сообщения 'Ошибка' под email"
        assert form.is_errored_fields_highlighted_red() == "rgb(255, 105, 114)", "Ожидался красный цвет границы при ошибке"

    @allure.title("Успешная авторизация пользователя")
    @pytest.mark.user_login
    def test_user_login_true(self, browser):

        page = MainPage(browser)
        page.open()
        page.go_to_enter_and_registration_form()

        form = RegistrationModal(browser)
        form.enter_existing_email(TestCredentials.EMAIL)
        form.enter_existing_user_password(TestCredentials.PASSWORD)
        form.submit_login_form_button()

        assert page.is_current_url_correct(suffix="login"), "Неверный URL после авторизации"
        assert page.is_user_avatar_displayed(), "Аватар не отображается"
        assert page.is_user_name_displayed(), "Имя пользователя не отображается"

    @allure.title("Успешный выход пользователя из аккаунта")
    @pytest.mark.user_login
    def test_user_logout_true(self, browser):

        page = MainPage(browser)
        page.open()
        page.go_to_enter_and_registration_form()

        form = RegistrationModal(browser)
        form.enter_existing_email(TestCredentials.EMAIL)
        form.enter_existing_user_password(TestCredentials.PASSWORD)
        form.submit_login_form_button()
        form.submit_logout_button()

        assert page.is_enter_and_registration_button_displayed(), "Должна отображаться кнопка 'Вход и регистрация' после логаута"
