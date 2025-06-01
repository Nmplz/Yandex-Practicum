from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
import allure


class OrderPage(BasePage):

    @allure.step("Кликаем по логотипу Самоката на странице заказа")
    def go_to_scooter_logo(self):
        self.click(OrderPageLocators.SCOOTER_LOGO)

    @allure.step("Заполняем поле 'Имя' на странице заказа: {name}")
    def fill_out_name_page_of_order(self, name):
        self.send_keys(locator=OrderPageLocators.NAME_FIELD, keys=name)

    @allure.step("Заполняем поле 'Фамилия' на странице заказа: {surname}")
    def fill_out_surname_page_of_order(self, surname):
        self.send_keys(locator=OrderPageLocators.SURNAME_FIELD, keys=surname)

    @allure.step("Заполняем поле 'Адрес' на странице заказа: {address}")
    def fill_out_address_page_of_order(self, address):
        self.send_keys(locator=OrderPageLocators.ADDRESS_FIELD, keys=address)

    @allure.step("Выбираем станцию метро: {station}")
    def select_metro_station_page_of_order(self, station):
        input_field = self.wait_for_clickable(OrderPageLocators.METRO_DROPDOWN)
        input_field.click()
        input_field.send_keys(station)
        option = self.wait_for_clickable(OrderPageLocators.select_metro_station_from_dropdown(station))
        option.click()

    @allure.step("Заполняем поле 'Телефон': {phone}")
    def fill_out_phone_page_of_order(self, phone):
        self.send_keys(locator=OrderPageLocators.PHONE_NUMBER_FIELD, keys=phone)

    @allure.step("Переходим на вторую страницу заказа")
    def go_to_the_second_page_of_order(self):
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполняем дату аренды: {date}")
    def fill_out_rent_date_of_order(self, date):
        input_field = self.find(OrderPageLocators.RENT_DATE_INPUT)
        input_field.send_keys(date)
        input_field.send_keys(Keys.ENTER)

    @allure.step("Выбираем срок аренды: 4 дня")
    def get_scooter_for_4_days(self):
        self.click(OrderPageLocators.RENT_TERMS_DROPDOWN)
        self.click(OrderPageLocators.RENT_TERMS_4_DAYS)

    @allure.step("Выбираем чёрный цвет самоката")
    def choose_scooter_black_color(self):
        self.click(OrderPageLocators.SCOOTER_COLOR_BLACK_CHECKBOX)

    @allure.step("Выбираем серый цвет самоката")
    def choose_scooter_grey_color(self):
        self.click(OrderPageLocators.SCOOTER_COLOR_GREY_CHECKBOX)

    @allure.step("Оставляем комментарий для курьера: {comment}")
    def fill_out_comment_for_courier(self, comment):
        self.send_keys(locator=OrderPageLocators.COMMENTS_FIELD, keys=comment)

    @allure.step("Нажимаем кнопку 'Заказать'")
    def make_an_order(self):
        self.click(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Проверяем появление модального окна подтверждения заказа")
    def check_is_complete_order_modal_appears(self):
        return self.is_element_present(OrderPageLocators.COMPLITE_ORDER_MODAL)
