from selenium.webdriver.common.by import By


class BasePageLocators:

    ENTER_AND_REGISTRATION_BUTTON = (By.CSS_SELECTOR, "button.buttonSecondary.inButtonText[type='button']")
    ENTER_MODAL_WINDOW = (By.XPATH, "//form[@class='popUp_shell__LuyqR' and contains(text(), 'Войти') ]")
    REGISTRATION_MODAL_WINDOW = (By.XPATH, "//form[@class='popUp_shell__LuyqR' and contains(text(), 'Зарегистрироваться')]")
    WARNING_AUTHORISATION_MODAL_WINDOW = (By.XPATH, "//h1[text()='Чтобы разместить объявление, авторизуйтесь']")


class RegistrationFormLocators:

    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[@type='button' and contains(text(), 'Нет аккаунта')]")
    ENTER_EMAIL = (By.CSS_SELECTOR, "input[placeholder='Введите Email']")
    ENTER_PASSWORD = (By.CSS_SELECTOR, "input[placeholder='Пароль']")
    ENTER_PASSWORD_REPITE = (By.CSS_SELECTOR, "input[placeholder='Повторите пароль']")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[@type='submit' and contains(text(), 'Создать аккаунт')]")
    ALLREADY_HAVE_ACCOUNT_BUTTON = (By.XPATH, "//button[@type='button' and contains(text(), 'Уже есть аккаунт')]")
    ERROR_MESSAGE = (By.XPATH, "//span[contains(@class, 'input_span') and text()='Ошибка']")
    ERROR_RED_BOX = (By.XPATH, "//input[@name='email']/parent::*")
    LOGIN_FORM_ENTER_BUTTON = (By.XPATH, "//button[@type='submit' and contains( text(), 'Войти')]")
    LOGIN_FORM_LOGOUT_BUTTON = (By.CSS_SELECTOR, 'button[class="spanGlobal btnSmall"]')


class MainPageLocators:

    PLACE_AD_BUTTON = (By.XPATH, "//button[@type='button' and contains(text(), 'Разместить объявление')]")
    AVATAR_IMAGE = (By.CSS_SELECTOR, "button.circleSmall")
    USER_NAME = (By.CSS_SELECTOR, "div.columnSmall h3.profileText.name")
    USER_PROFILE_AD_NAME = (By.XPATH, ".//h2")
    USER_PROFILE_AD_CITY = (By.XPATH, ".//h3")
    USER_PROFILE_AD_PRICE = (By.XPATH, ".//div[@class='price']/h2")

    @staticmethod
    def user_profile_ad_card(title):
        return (By.XPATH, f"//div[@class='card'][.//h2[text()='{title}']]")
    



class NewAdvertisementPageLocators:

    PRODUCT_NAME_FIELD = (By.CSS_SELECTOR, 'input[placeholder="Название"]')
    PRODUCT_DISCRIPTION_FIELD = (By.CSS_SELECTOR, 'textarea[placeholder="Описание товара"]')
    PRODUCT_PRICE_FIELD = (By.CSS_SELECTOR, 'input[placeholder="Стоимость"]')
    CATEGORY_DROP_DOWN_MENU = (By.XPATH, "//input[@name='category']/following-sibling::button")
    CATEGORY_DROP_DOWN_MENU_TECHNOLOGY = (By.XPATH, "//button[contains(@class, 'dropDownMenu_btn')][.//span[text()='Технологии']]")
    CITY_DROPDOWN_MENU = (By.XPATH, "//input[@name='city']/following-sibling::button")
    CITY_DROPDOWN_MENU_KAZAN = (By.XPATH, "//button[contains(@class, 'dropDownMenu_btn')][.//span[text()='Казань']]")
    PRODUCT_CONDITION_NEW_RADIO = (By.CSS_SELECTOR, 'div[class="radioUnput_inputActive__eC-HY"]')
    PRODUCT_CONDITION_USED_RADIO = (By.CSS_SELECTOR, 'div[class="radioUnput_inputRegular__FbVbr"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
