from pages.locators import MainPageLocators, BasePageLocators
from pages.base_page import BasePage
import allure



class MainPage(BasePage):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @allure.step("Проверяем, что текущий URL совпадает с ожидаемым суффиксом: {suffix}")
    def is_current_url_correct(self, suffix=""):
        print("self.current_url>>>>>", self.current_url)
        print(f"{self.BASE_URL}/{suffix}", "BASE URL<<<<<<<")
        return self.current_url() == f"{self.BASE_URL}/{suffix}"

    @allure.step("Проверяем отображение кнопки 'Вход и регистрация'")
    def is_enter_and_registration_button_displayed(self):
        return self.is_element_present(BasePageLocators.ENTER_AND_REGISTRATION_BUTTON)

    @allure.step("Проверяем, что отображается аватар пользователя")
    def is_user_avatar_displayed(self):
        self.wait_for_clickable(MainPageLocators.AVATAR_IMAGE)
        avatar = self.is_element_present(MainPageLocators.AVATAR_IMAGE)
        return avatar

    @allure.step("Проверяем, что отображается имя пользователя")
    def is_user_name_displayed(self):
        self.wait_for_clickable(MainPageLocators.USER_NAME)
        name = self.is_element_with_text_present(*MainPageLocators.USER_NAME, "User.")
        return name

    @allure.step("Нажимаем на кнопку 'Разместить объявление'")
    def click_place_ad_button(self, expect_page_reload=False):
        if expect_page_reload:
            old_button = self.find(MainPageLocators.PLACE_AD_BUTTON)
            self.wait_until_stale(old_button)

        self.click(MainPageLocators.PLACE_AD_BUTTON)

    @allure.step("Переход в профиль пользователя")
    def go_to_user_profile(self):

        old_button = self.find(MainPageLocators.AVATAR_IMAGE)
        self.wait_until_stale(old_button)
        self.click(MainPageLocators.AVATAR_IMAGE)

    @allure.step("Получаем информацию об объявлении с названием: {title}")
    def get_ad_info_by_title(self, title):

        self.wait_for_presence(MainPageLocators.user_profile_ad_card(title))

        ad_card = self.find(MainPageLocators.user_profile_ad_card(title))
        name = ad_card.find_element(*MainPageLocators.USER_PROFILE_AD_NAME).text
        city = ad_card.find_element(*MainPageLocators.USER_PROFILE_AD_CITY).text
        price_text = ad_card.find_element(*MainPageLocators.USER_PROFILE_AD_PRICE).text

        price = int(price_text.replace("₽", "").replace(" ", "").strip())

        return name, city, price
