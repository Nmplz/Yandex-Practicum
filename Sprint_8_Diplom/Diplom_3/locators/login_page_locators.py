from selenium.webdriver.common.by import By


class LoginPageLocators:

    RESTORE_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
    EMAIL_FIELD = (By.XPATH, '//label[text()="Email"]/following-sibling::input')
    PASSWORD_FIELD = (By.XPATH, '//input[@type="password"]')
    ENTER_BUTTON = (By.XPATH, '//button[text()="Войти"]')