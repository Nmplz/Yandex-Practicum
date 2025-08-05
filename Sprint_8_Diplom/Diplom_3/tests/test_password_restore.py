import allure

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.restore_password_page import RestorePasswordPage
from data.urls import Urls


@allure.story("Проверка восстановления пароля")
class TestPasswordRestore:

    @allure.title("Переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_navigate_to_password_recovery_page(self, browser):
        page = MainPage(browser)
        page.open()
        page.press_login_button()
        page = LoginPage(browser)
        page.go_to_restore_password_link()
        assert page.current_url() == Urls.RESTORE_PASSWORD_URl, f"{page.current_url()}< URL Не совпадает с ожидаемым"

    @allure.title("Ввод почты и клик по кнопке «Восстановить»")
    def test_enter_email_and_click_restore_button(self, browser):
        page = MainPage(browser)
        page.open()
        page.press_login_button()
        page = LoginPage(browser)
        page.go_to_restore_password_link()
        page = RestorePasswordPage(browser)
        page.enter_email_and_confirm()
        assert page.current_url() == Urls.RESET_PASSWORD_URL, f"{page.current_url()}< URL Не совпадает с ожидаемым"

    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его")
    def test_click_show_password_highlights_input_field(self, browser):
        page = MainPage(browser)
        page.open()
        page.press_login_button()
        page = LoginPage(browser)
        page.go_to_restore_password_link()
        page = RestorePasswordPage(browser)
        page.enter_email_and_confirm()
        page.click_shows_password_icon()
        assert page.check_is_password_field_active(), "Поле не получило фокус после клика на глаз"
