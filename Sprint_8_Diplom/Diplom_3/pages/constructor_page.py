import allure

from locators.constructor_page_locators import ConstructorPageLocators
from pages.base_page import BasePage


class ConstructorPage(BasePage):

    @allure.step("Выбор ингридиента Краторная булка N-200i")
    def select_ingredient_bun(self):
        self.click(ConstructorPageLocators.INGREDIENT_BUN)

    @allure.step("Проверка появления модального окна Детали ингредиента")
    def check_details_modal_window_appear(self):
        return self.wait_for_presence(ConstructorPageLocators.INGREDIENT_DETAILS_MODAL_TITLE)

    @allure.step("Закрытие модального окна Детали ингредиента")
    def close_details_modal_window(self):
        self.click(ConstructorPageLocators.MODAL_CLOSE_BUTTON)
        return self.wait_for_invisibility(ConstructorPageLocators.INGREDIENT_DETAILS_MODAL_TITLE)

    @allure.step("Добавление булки в корзину")
    def add_bun_to_order_cart(self):
        source_elem = self.find(ConstructorPageLocators.INGREDIENT_BUN)
        target_elem = self.find(ConstructorPageLocators.ORDER_CART)
        self.drag_and_drop_element(source_elem, target_elem)

    @allure.step("Проверка счетчика ингридиентов")
    def count_number_of_ingredients(self):
        return self.find(ConstructorPageLocators.INGREDIENT_COUNTER).text

    @allure.step("Создание заказа")
    def create_an_order(self):
        self.wait_for_clickable(ConstructorPageLocators.INGREDIENT_BUN)
        bun_elem = self.find(ConstructorPageLocators.INGREDIENT_BUN)
        cart_elem = self.find(ConstructorPageLocators.ORDER_CART)
        self.drag_and_drop_element(bun_elem, cart_elem)
        sause_elem = self.find(ConstructorPageLocators.INGREDIENT_SAUCE)
        self.drag_and_drop_element(sause_elem, cart_elem)
        filling_elem = self.find(ConstructorPageLocators.INGREDIENT_FILLING)
        self.drag_and_drop_element(filling_elem, cart_elem)
        self.forse_click(ConstructorPageLocators.ORDER_CREATE_BUTTON)
        self.wait_for_clickable(ConstructorPageLocators.ORDER_MODAL_FRAME)
        self.wait_for_invisibility(ConstructorPageLocators.DEFAULT_ORDER_NUMBER)
        self.wait_for_visible(ConstructorPageLocators.ORDER_IS_PREPARING_TEXT)
        order_number = self.wait_for_clickable(ConstructorPageLocators.REAL_ORDER_NUMBER).text
        self.forse_click(ConstructorPageLocators.CLOSE_ORDER_MENU_BUTTON)
        return order_number

    @allure.step("Ожидание окна созданного заказа")
    def is_order_confirmation_modal_appear(self):
        return self.wait_for_visible(ConstructorPageLocators.ORDER_IS_PREPARING_TEXT)

    @allure.step("Переход по кнопке Лента Заказов")
    def go_to_orders_feed_button(self):
        self.forse_click(ConstructorPageLocators.ORDER_FEED_BUTTON)
