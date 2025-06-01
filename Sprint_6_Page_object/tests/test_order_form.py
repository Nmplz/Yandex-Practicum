import pytest
from utils.data_loader import load_test_data
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.urls import Urls
import allure


class TestOrderForm:

    @allure.title("Переход по верхней кнопке 'Заказать' ведёт на страницу заказа")
    def test_top_order_button_leads_to_order_page(self, browser):

        page = MainPage(browser)
        page.open()
        page.go_to_top_order_button()
        assert page.current_url() == Urls.ORDER_PAGE_URL, f"Верняя кнопка заказа ведёт на неправильную страницу"

    @allure.title("Переход по нижней кнопке 'Заказать' ведёт на страницу заказа")
    def test_bottom_order_button_leads_to_order_page(self, browser):

        page = MainPage(browser)
        page.open()
        page.go_to_bottom_order_button()
        assert page.current_url() == Urls.ORDER_PAGE_URL, f"Нижняя кнопка заказа ведёт на неправильную страницу"

    @allure.title("Позитивный сценарий оформления заказа через верхнюю кнопку (параметризованный)")
    @pytest.mark.parametrize("user_data", load_test_data())
    def test_place_test_order(self, browser, user_data):
        name = user_data["name"]
        surname = user_data["surname"]
        address = user_data["address"]
        metro = user_data["metro"]
        phone = user_data["phone"]
        rent_date = user_data["rent_date"]
        comment = user_data["comment"]

        page = MainPage(browser)
        page.open()
        page.go_to_top_order_button()

        page = OrderPage(browser)
        page.fill_out_name_page_of_order(name)
        page.fill_out_surname_page_of_order(surname)
        page.fill_out_address_page_of_order(address)
        page.select_metro_station_page_of_order(metro)
        page.fill_out_phone_page_of_order(phone)
        page.go_to_the_second_page_of_order()
        page.fill_out_rent_date_of_order(rent_date)
        page.get_scooter_for_4_days()
        page.choose_scooter_black_color()
        page.fill_out_comment_for_courier(comment)
        page.make_an_order()
        result = page.check_is_complete_order_modal_appears()
        assert result, f"Complete order modal doesnt appears"

    @allure.title("Клик по логотипу Самоката ведёт на главную страницу")
    def test_scooter_logo_leads_to_dzen(self, browser):

        page = MainPage(browser)
        page.open()
        page.go_to_top_order_button()
        page = OrderPage(browser)
        page.go_to_scooter_logo()
        curr_page = page.current_url()
        assert curr_page == Urls.BASE_URL, f"Scooter logo leads the wrong path --> {curr_page}"

    @allure.title("Клик по логотипу Яндекса открывает Дзен в новой вкладке")
    def test_yandex_logo_leads_to_dzen(self, browser):

        page = MainPage(browser)
        page.open()
        page.go_to_yandex_logo()
        tabs = page.all_tabs_list()
        page.switch_to_tab(tabs[-1])
        page.wait_for_yandex_page_download()
        curr_page = page.current_url()
        assert curr_page == Urls.REDIRECT_URL, f'Yandex logo leads the wrong path --> {curr_page}"'
