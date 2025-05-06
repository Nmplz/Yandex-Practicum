from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators

class BasePage:

    BASE_URL = 'https://qa-desk.stand.praktikum-services.ru'

    def __init__(self, browser, timeout=10):
        self.browser = browser
        self.wait = WebDriverWait(browser, timeout)


    def open(self, url_suffix=""):
        self.browser.get(self.BASE_URL + url_suffix)

    def go_to_enter_and_registration_form(self):
        # WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(BasePageLocators.ENTER_AND_REGISTRATION_BUTTON)).click()
        self.click(BasePageLocators.ENTER_AND_REGISTRATION_BUTTON)

        
    def current_url(self):
        return self.browser.current_url

    def find(self, locator):
        return self.browser.find_element(*locator)

    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click(self, locator):
        self.wait_for_clickable(locator).click()

    def wait_until_stale(self, element):
        self.wait.until(EC.staleness_of(element))

    def wait_for_presence(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def is_element_present(self, locator):
        try:
            self.wait_for_presence(locator)
        except NoSuchElementException:
            return False
        return True    
    
    def is_element_with_text_present(self, how, what, text):
        try:
            elements = self.browser.find_elements(how, what)
            for element in elements:
                if element.text == text:
                    return True
            raise Exception(f"There is No such element '{what}' with text '{text}'")
        except NoSuchElementException:
            return False