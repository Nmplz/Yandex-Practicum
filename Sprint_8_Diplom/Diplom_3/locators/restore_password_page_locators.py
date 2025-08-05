from selenium.webdriver.common.by import By


class RestorePasswordPageLocators:

    EMAIL_FIELD = (By.XPATH, '//label[text()="Email"]/following-sibling::input')
    RESTORE_PASSWORD_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    NEW_PASSWORD_CONFIRM_BUTTON = (By.XPATH, "//button[text()='Сохранить']")
    SHOW_PASSWORD_TOGGLE = (By.XPATH, '//div[contains(@class,"icon-action")]')
    PASSWORD_FIELD_IS_ACTIVE = (By.CSS_SELECTOR, ".input.input_status_active")
