import pytest
import allure
from pages.main_page import MainPage
from pages.registration_modal import RegistrationModal
from pages.new_ad_page import NewAdvertisementPage
from data import TestCredentials


class TestPlaceAdvertisement:

    @allure.title("Нельзя создать объявление без авторизации")
    @pytest.mark.place_ad
    def test_create_ad_without_authentication_false(self, browser):

        page = MainPage(browser)
        page.open()
        page.click_place_ad_button()
        form = RegistrationModal(browser)

        assert form.is_modal_with_warring_displayed(), "Не появилось модальное окно с заголовком «Чтобы разместить объявление, авторизуйтесь»"

    @allure.title("Успешное создание объявления после авторизации")
    def test_create_ad_with_authentication_true(self, browser):

        page = MainPage(browser)
        page.open()
        page.go_to_enter_and_registration_form()

        form = RegistrationModal(browser)
        form.enter_existing_email(TestCredentials.EMAIL)
        form.enter_existing_user_password(TestCredentials.PASSWORD)
        form.submit_login_form_button()
        page.click_place_ad_button(expect_page_reload=True)

        page_ad = NewAdvertisementPage(browser)
        product_name = page_ad.fill_product_name_form()
        product_price = page_ad.fill_product_price()
        page_ad.fill_product_disc_form()
        page_ad.set_product_category()
        product_city = page_ad.set_product_city()
        page_ad.set_product_condition_to_used()
        page_ad.click_submit_button()
        page.go_to_user_profile()

        name, city, price = page.get_ad_info_by_title(product_name)

        assert name == product_name, f"Название товара > {name}, не соответствует ожидаемому > {product_name}"
        assert city == product_city, f"Название города > {city}, не соответствует ожидаемому > {product_city}"
        assert price == product_price, f"Цена > {price}, не соответствует ожидаемой > {price}"
