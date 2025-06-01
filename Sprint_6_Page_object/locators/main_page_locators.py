from selenium.webdriver.common.by import By


class MainPageLocators:

    FAQ_MENU = (By.CSS_SELECTOR, "div.Home_FourPart__1uthg")
    YANDEX_LOGO =(By.CSS_SELECTOR, "a.Header_LogoYandex__3TSOI")
    YANDEX_POP_UP = (By.CSS_SELECTOR, ".yc7d11a87")
    SCOOTER_LOGO = (By.CSS_SELECTOR, "a.Header_LogoScooter__3lsAR")

    ORDER_BUTTON_TOP = (By.CSS_SELECTOR, "div.Header_Nav__AGCXC button.Button_Button__ra12g")
    ORDER_BUTTON_BOTTOM = (By.CSS_SELECTOR, "div.Home_FinishButton__1_cWm button.Button_Button__ra12g")

    Q1_HOW_MUCH_DOES_IT_COST = (By.CSS_SELECTOR, "#accordion__heading-0")
    Q1_ANSWER = (By.CSS_SELECTOR, "#accordion__panel-0")

    Q2_I_WANT_SOME_SCOOTERS = (By.CSS_SELECTOR, "#accordion__heading-1")
    Q2_ANSWER = (By.CSS_SELECTOR, "#accordion__panel-1")

    Q3_TIME_TO_RENT = (By.CSS_SELECTOR, "#accordion__heading-2")
    Q3_ANSWER = (By.CSS_SELECTOR, "#accordion__panel-2")

    Q4_RENT_FOR_TODAY = (By.CSS_SELECTOR, "#accordion__heading-3")
    Q4_ANSWER = (By.CSS_SELECTOR, "#accordion__panel-3")

    Q5_RENT_FOR_MORE_TIME = (By.CSS_SELECTOR, "#accordion__heading-4")
    Q5_ANSWER = (By.CSS_SELECTOR, "#accordion__panel-4")

    Q6_DO_YOU_BRING_CHARGER = (By.CSS_SELECTOR, "#accordion__heading-5")
    Q6_ANSWER = (By.CSS_SELECTOR, "#accordion__panel-5")

    Q7_CAN_I_CANSEL_ORDER = (By.CSS_SELECTOR, "#accordion__heading-6")
    Q7_ANSWER = (By.CSS_SELECTOR, "#accordion__panel-6")

    Q8_DO_YOU_DELIVER_OUTSIDE_MKAD = (By.CSS_SELECTOR, "#accordion__heading-7")
    Q8_ANSWER = (By.CSS_SELECTOR, "#accordion__panel-7")
