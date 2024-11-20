from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    FIELD_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    FIELD_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    FIELD_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_SUBMIT = (By.CSS_SELECTOR, "button[name=\"registration_submit\"]")


class ProductPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_ABOUT_ADD_TO_BASKET = (By.CSS_SELECTOR, "#messages>div:nth-child(1)>.alertinner strong")
    MESSAGE_ABOUT_BASKET_TOTAL = (By.CSS_SELECTOR, "#messages>div:nth-child(3)>.alertinner strong")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group a[class=\"btn btn-default\"]")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner>p")
    ITEMS_IN_THE_BASKET = (By.CSS_SELECTOR, ".basket-items")
