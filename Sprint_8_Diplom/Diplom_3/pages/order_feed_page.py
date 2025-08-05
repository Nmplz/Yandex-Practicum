import allure

from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):
    
    @allure.step('Выбор последнего созданного заказа')
    def select_last_order(self):
        self.click(OrderFeedPageLocators.ORDER_IN_FEED_LINK)

    @allure.step('Проверка появления модального окна при выборе заказа')
    def is_order_modal_appear(self):
        return self.wait_for_visible(OrderFeedPageLocators.ORDER_MODAL_CONTENTS_TITLE)
    
    @allure.step("Найти заказ в ленте заказов")
    def find_order_in_order_list(self, order_number):
        return self.wait_for_clickable(OrderFeedPageLocators.get_order_in_order_feed(order_number))
    
    @allure.step("Переход по кнопке Конструктор")
    def go_to_constructor_button(self):
        self.click(OrderFeedPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Получить значение счетчика Выполнено за всё время")
    def get_total_orders_number(self):
        self.wait_for_clickable(OrderFeedPageLocators.COMPLETE_ORDERS_TOTAL_COUNTER)
        return self.wait_for_visible(OrderFeedPageLocators.COMPLETE_ORDERS_TOTAL_COUNTER).text

    @allure.step("Получить значение счетчика Выполнено за сегодня")
    def get_today_orders_number(self):
        self.wait_for_clickable(OrderFeedPageLocators.COMPLETE_ORDERS_TODAY_COUNTER)
        return self.wait_for_visible(OrderFeedPageLocators.COMPLETE_ORDERS_TODAY_COUNTER).text

    @allure.step("Получить значение счетчика В работе")
    def get_order_number_in_work_list(self):
        self.wait_for_clickable(OrderFeedPageLocators.ORDER_NUMBER_IN_WORK)
        return self.wait_for_visible(OrderFeedPageLocators.ORDER_NUMBER_IN_WORK).text
