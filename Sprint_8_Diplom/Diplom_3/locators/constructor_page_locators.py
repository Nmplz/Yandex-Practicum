from selenium.webdriver.common.by import By


class ConstructorPageLocators:

    INGREDIENT_BUN = (By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa6c"]')
    INGREDIENT_FILLING = (By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa77"]')
    INGREDIENT_SAUCE = (By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa74"]')
    INGREDIENT_DETAILS_MODAL_TITLE = (By.XPATH, '//h2[text()="Детали ингредиента"]')
    MODAL_CLOSE_BUTTON = (By.XPATH, '//button[contains(@class,"close")]')
    INGREDIENT_COUNTER = (By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa6c"]//p[contains(@class, "counter__num")]')
    ORDER_CART = (By.XPATH, '//ul[contains(@class,"basket")]')
    ORDER_CREATE_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')
    ORDER_IS_PREPARING_TEXT = (By.XPATH, '//p[text()="Ваш заказ начали готовить"]')
    ORDER_FEED_BUTTON = (By.XPATH, '//p[text()="Лента Заказов"]/parent::a')
    ORDER_PREPARING_TEXT = (By.XPATH, '//p[text()="Ваш заказ начали готовить"]')
    DEFAULT_ORDER_NUMBER = (By.XPATH, '//h2[text()="9999"]')
    REAL_ORDER_NUMBER = (By.XPATH, '//h2[contains(@class, "type_digits-large")]')
    CLOSE_ORDER_MENU_BUTTON = (By.XPATH, '//button[contains(@class,"close")]')
    ORDER_MODAL_FRAME = (By.XPATH, '//div[contains(@class,"Modal_modal__container__Wo2l_")]')


