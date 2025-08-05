import allure

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from data.urls import Urls



class BasePage:

    BASE_URL = Urls.BASE_URL

    def __init__(self, browser, timeout=10):
        self.browser = browser
        self.wait = WebDriverWait(browser, timeout)
        self.browser_name = self.browser.capabilities["browserName"].lower()

    def open(self, url_suffix=""):
        self.browser.get(self.BASE_URL + url_suffix)

    def current_url(self):
        return self.browser.current_url

    def save_current_tab(self):
        return self.browser.current_window_handle

    def all_tabs_list(self):
        return self.browser.window_handles

    def switch_to_tab(self, tab):
        self.browser.switch_to.window(tab)

    def click(self, locator):
        self.wait_for_clickable(locator).click()

    def send_keys(self, locator, keys):
        self.wait_for_clickable(locator).send_keys(keys)

    def find(self, locator):
        return self.browser.find_element(*locator)

    def forse_click(self, locator):
        element = self.find(locator)
        self.browser.execute_script("arguments[0].click();", element)

    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def scroll_to_element(self, locator):
        element = self.find(locator)
        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def wait_for_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_until_stale(self, element):
        self.wait.until(EC.staleness_of(element))

    def wait_for_invisibility(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def wait_for_presence(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_about_blank(self):
        self.wait.until(lambda d: d.current_url != "about:blank")

    def is_element_present(self, locator):
        try:
            self.wait_for_presence(locator)
        except NoSuchElementException:
            return False
        return True

    @allure.step("Кликнуть на элемент в FFox")
    def click_on_element(self, locator):
        target = self.wait_for_visible(locator)
        click = ActionChains(self.browser)
        click.move_to_element(target).click().perform()

    @allure.step("Проверить отображение элемента")
    def check_displaying_of_element(self, locator):
        return self.browser.find_element(*locator).is_displayed()

    @allure.step("Перетаскивание элемента на странице")
    def drag_and_drop_element(self, source_element, target_element):
        script = """
            function simulateHTML5DragAndDrop(sourceNode, destinationNode) {
                var dataTransfer = new DataTransfer();
                var dragStartEvent = new DragEvent('dragstart', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                sourceNode.dispatchEvent(dragStartEvent);

                var dropEvent = new DragEvent('drop', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                destinationNode.dispatchEvent(dropEvent);
                var dragEndEvent = new DragEvent('dragend', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                sourceNode.dispatchEvent(dragEndEvent);
            }
            simulateHTML5DragAndDrop(arguments[0], arguments[1]);
            """
        self.browser.execute_script(script, source_element, target_element)
