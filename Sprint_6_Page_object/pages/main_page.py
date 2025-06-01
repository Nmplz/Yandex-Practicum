from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
import allure


class MainPage(BasePage):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @allure.step("Кликаем по верхней кнопке 'Заказать'")
    def go_to_top_order_button(self):
        self.click(MainPageLocators.ORDER_BUTTON_TOP)

    @allure.step("Скроллим к нижней кнопке 'Заказать' и кликаем по ней")
    def go_to_bottom_order_button(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.click(MainPageLocators.ORDER_BUTTON_BOTTOM)

    @allure.step("Скроллим к разделу с вопросами (FAQ)")
    def go_to_faq_menu(self):
        self.scroll_to_element(MainPageLocators.FAQ_MENU)

    @allure.step("Кликаем по логотипу Яндекса")
    def go_to_yandex_logo(self):
        self.click(MainPageLocators.YANDEX_LOGO)

    @allure.step("Получаем текст вопроса и ответ по локаторам")
    def get_question_and_answer(self, question_locator, answer_locator):
        question_text = self.find(question_locator).text
        self.click(question_locator)
        self.wait_for_visible(answer_locator)
        answer_text = self.find(answer_locator).text
        return question_text, answer_text

    @allure.step("Ожидаем загрузку страницы Яндекса и появление попапа")
    def wait_for_yandex_page_download(self):
        self.wait_for_about_blank()
        self.wait_for_presence(MainPageLocators.YANDEX_POP_UP)