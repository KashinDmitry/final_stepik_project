from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_ADDED_MESSAGE = (By.CSS_SELECTOR, ".alert-success:first-child")
    PRODUCT_NAME_IN_ADDED_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, ".alert-success:first-child strong")
    YOUR_BASKET_TOTAL_NOTIFICATION = (By.CSS_SELECTOR, ".alert-info")
    BASKET_PRICE_IN_BASKET_TOTAL_NOTIFICATION = (By.CSS_SELECTOR, ".alert-info strong")