from selenium.webdriver.common.by import By

class OrderFeedPageLocators:

    ORDER_IN_FEED_LINK = (By.XPATH, '//*[contains(@class, "OrderHistory_link")]')
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text()="Конструктор"]/parent::a')
    ORDER_MODAL_CONTENTS_TITLE = (By.XPATH, '//p[text()="Cостав"]')
    COMPLETE_ORDERS_TODAY_COUNTER = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p[contains(@class,"digits-large")]')
    COMPLETE_ORDERS_TOTAL_COUNTER = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p[contains(@class,"digits-large")]')
    ORDER_NUMBER_IN_WORK = (By.XPATH, '//*[contains(@class,"orderListReady")]//li[contains(@class,"digits-default")]')
  

    @staticmethod
    def get_order_in_order_feed(order_number):
        return (By.XPATH, f"//p[text()='{order_number}']")