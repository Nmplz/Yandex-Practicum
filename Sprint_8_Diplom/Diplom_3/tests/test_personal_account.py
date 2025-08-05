import allure

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from data.urls import Urls


@allure.story("Проверка Личного кабинета")
class TestPersonalAccount:

    @allure.title("Переход в Личный кабинет по клику на «Личный кабинет»")
    def test_navigate_to_profile_from_main_page(self, browser, login_user):
        page = MainPage(browser)
        page.go_to_profile_after_auth()
        assert page.current_url() == Urls.USER_ACCOUNT_URL

    @allure.title("Переход в раздел «История заказов» из профиля")
    def test_navigate_to_order_history_from_profile(self, browser, login_user):
        page = MainPage(browser)
        page.go_to_profile_after_auth()
        page = AccountPage(browser)
        page.press_order_history_menu()
        assert page.current_url() == Urls.USER_ACCOUNT_HISTORY_URL

    @allure.title("Выход из аккаунта через личный кабинет")
    def test_logout_from_profile_page(self, browser, login_user):
        page = MainPage(browser)
        page.go_to_profile_after_auth()
        page = AccountPage(browser)
        page.test_logout_from_account()
        assert page.current_url() == Urls.LOGIN_PAGE_URL
