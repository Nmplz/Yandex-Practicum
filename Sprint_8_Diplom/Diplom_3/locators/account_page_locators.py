from selenium.webdriver.common.by import By


class AccountPageLocators:

    ORDER_HISTORY_LINK = (By.XPATH, '//*[@href="/account/order-history"]')
    LOGOUT_BUTTON = (By.XPATH, '//*[contains(@class, "Account_button")]')
    