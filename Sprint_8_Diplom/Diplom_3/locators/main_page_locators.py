from selenium.webdriver.common.by import By


class MainPageLocators:

    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    PROFILE_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    OVERLAY_LAYOUT = (By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text()="Конструктор"]/parent::a')
    ORDER_FEED_BUTTON = (By.XPATH, '//p[text()="Лента Заказов"]/parent::a')