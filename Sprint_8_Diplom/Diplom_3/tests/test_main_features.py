import allure

from pages.main_page import MainPage
from pages.constructor_page import ConstructorPage
from data.urls import Urls


@allure.story("Проверка основного функционала")
class TestMainFeatures:

    @allure.title("Переход по клику на «Конструктор»")
    def test_redirect_by_constructor_button(self, browser):
        page = MainPage(browser)
        page.open("login")
        page.go_to_constructor_button()
        assert page.current_url() == Urls.BASE_URL

    @allure.title("Переход по клику на «Лента заказов»")
    def test_redirect_by_order_list_button(self, browser):
        page = MainPage(browser)
        page.open()
        page.go_to_orders_feed_button()
        assert page.current_url() == Urls.ORDER_FEED_URL

    @allure.title("Если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_get_ingredient_details_modal(self, browser):
        page = ConstructorPage(browser)
        page.open()
        page.select_ingredient_bun()
        assert page.check_details_modal_window_appear(), "Окно «Детали ингредиента» не появилось"

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_close_ingredient_details_window(self, browser):
        page = ConstructorPage(browser)
        page.open()
        page.select_ingredient_bun()
        page.check_details_modal_window_appear()
        assert page.close_details_modal_window(), "Окно «Детали ингредиента» не закрылось"

    @allure.title("При добавлении ингредиента в заказ счётчик этого ингридиента увеличивается")
    def test_ingredient_counter_change(self, browser):
        page = ConstructorPage(browser)
        page.open()
        page.add_bun_to_order_cart()
        counter = page.count_number_of_ingredients()
        assert counter == "2", "Неверное значение счетчика ингридиентов"

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_successful_order_from_auth_user(self, browser, login_user):

        page = ConstructorPage(browser)
        order_number = page.create_an_order()
        assert order_number, "Создание заказа прошло с ошибкой, не был получен номер заказа"
