import allure
from pages.base_page import BasePage
from pages.locators import NewAdvertisementPageLocators
from utils.generators import generate_unique_title


class NewAdvertisementPage(BasePage):

    @allure.step("Заполняем поле названия товара уникальным значением")
    def fill_product_name_form(self):

        name = generate_unique_title("ProductUniqueName")

        link = self.find(NewAdvertisementPageLocators.PRODUCT_NAME_FIELD)
        link.send_keys(name)
        return name

    @allure.step("Заполняем поле описания товара уникальным значением")
    def fill_product_disc_form(self):

        disc = generate_unique_title("ProductUniqueDiscription")
        link = self.find(NewAdvertisementPageLocators.PRODUCT_DISCRIPTION_FIELD)
        link.send_keys(disc)
        return disc

    @allure.step("Заполняем поле цены значением: 100500")
    def fill_product_price(self):
        price = 100500
        link = self.find(NewAdvertisementPageLocators.PRODUCT_PRICE_FIELD)
        link.send_keys(price)
        return price

    @allure.step("Выбираем категорию товара: Технологии")
    def set_product_category(self):
        category_dropdown = self.click(NewAdvertisementPageLocators.CATEGORY_DROP_DOWN_MENU)
        set_tech_category = self.click(NewAdvertisementPageLocators.CATEGORY_DROP_DOWN_MENU_TECHNOLOGY)

    @allure.step("Выбираем город подачи объявления: Казань")
    def set_product_city(self):
        city_dropdown = self.click(NewAdvertisementPageLocators.CITY_DROPDOWN_MENU)
        set_city_kazan = self.click(NewAdvertisementPageLocators.CITY_DROPDOWN_MENU_KAZAN)
        return f"Казань"

    @allure.step("Устанавливаем состояние товара: Б/У")
    def set_product_condition_to_used(self):
        self.click(NewAdvertisementPageLocators.PRODUCT_CONDITION_USED_RADIO)

    @allure.step("Нажимаем на кнопку 'Подать объявление'")
    def click_submit_button(self):
        self.click(NewAdvertisementPageLocators.SUBMIT_BUTTON)
