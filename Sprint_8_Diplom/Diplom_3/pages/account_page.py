import allure

from locators.account_page_locators import AccountPageLocators
from pages.base_page import BasePage


class AccountPage(BasePage):

    @allure.step("Нажать на меню «История заказов»")
    def press_order_history_menu(self):
        self.click(AccountPageLocators.ORDER_HISTORY_LINK)

    @allure.title("Выход из аккаунта")
    def test_logout_from_account(self):
        self.click(AccountPageLocators.LOGOUT_BUTTON)
        self.wait_for_invisibility(AccountPageLocators.LOGOUT_BUTTON)
