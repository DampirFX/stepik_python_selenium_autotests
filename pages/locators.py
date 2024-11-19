from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_ABOUT_ADD_TO_BASKET = (By.CSS_SELECTOR,"#messages>div:nth-child(1)>.alertinner strong")
    MESSAGE_ABOUT_BASKET_TOTAL = (By.CSS_SELECTOR, "#messages>div:nth-child(3)>.alertinner strong")


    # .alertinner p:nth-child(1)