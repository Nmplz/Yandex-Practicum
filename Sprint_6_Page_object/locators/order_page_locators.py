from selenium.webdriver.common.by import By


class OrderPageLocators:

    NAME_FIELD = (By.CSS_SELECTOR, 'input[placeholder="* Имя"]')
    SURNAME_FIELD = (By.CSS_SELECTOR, 'input[placeholder="* Фамилия"]')
    ADDRESS_FIELD = (By.CSS_SELECTOR, 'input[placeholder="* Адрес: куда привезти заказ"]')
    PHONE_NUMBER_FIELD = (By.CSS_SELECTOR, 'input[placeholder="* Телефон: на него позвонит курьер"]')
    METRO_DROPDOWN = (By.CSS_SELECTOR, ".select-search__input")
    NEXT_BUTTON = (By.CSS_SELECTOR, 'button[class*="Button_Middle__1CSJM"]')
    RENT_DATE_INPUT = (By.CSS_SELECTOR, 'input[placeholder="* Когда привезти самокат"]')
    RENT_TERMS_DROPDOWN = (By.CSS_SELECTOR, 'div[class="Dropdown-control"]')
    RENT_TERMS_4_DAYS = (By.XPATH, "//div[@class='Dropdown-option' and text()='четверо суток']")
    SCOOTER_COLOR_BLACK_CHECKBOX = (By.CSS_SELECTOR, "div.Order_Checkboxes__3lWSI #black")
    SCOOTER_COLOR_GREY_CHECKBOX = (By.CSS_SELECTOR, "div.Order_Checkboxes__3lWSI #grey")
    COMMENTS_FIELD = (By.CSS_SELECTOR, 'input[placeholder="Комментарий для курьера"]')
    ORDER_BUTTON = (By.CSS_SELECTOR, 'button[class="Button_Button__ra12g Button_Middle__1CSJM"]')
    COMPLITE_ORDER_MODAL = (By.CSS_SELECTOR, 'div[class="Order_Text__2broi"]')
    SCOOTER_LOGO = (By.CSS_SELECTOR, "a.Header_LogoScooter__3lsAR")

    @staticmethod
    def select_metro_station_from_dropdown(station):
        return (By.XPATH, f"//button[.='{station}']")
