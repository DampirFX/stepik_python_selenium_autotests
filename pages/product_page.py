from .base_page import BasePage
from .locators import  ProductPageLocators


class ProductPage(BasePage):
    def get_product_name(self):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return name

    def get_product_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return price

    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.PRODUCT_BUTTON_ADD_TO_BASKET)
        button.click()

    def get_product_name_from_message(self):
        name = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADD_TO_BASKET).text
        #  has been added to your basket.
        return name

    def get_product_price_from_message(self):
        price = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_BASKET_TOTAL).text
        # Your basket total is now
        return price

    def should_be_present_button_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_BUTTON_ADD_TO_BASKET), "Button add to basket is not presented"

    def should_be_present_message_about_adding_to_basket(self):
        assert self.is_element_present(
            *ProductPageLocators.MESSAGE_ABOUT_ADD_TO_BASKET), "Message about add to basket is not presented"

    def should_be_present_message_about_basket_total(self):
        assert self.is_element_present(
            *ProductPageLocators.MESSAGE_ABOUT_BASKET_TOTAL), "Message about basket total is not presented"

    def names_should_be_equal(self, name, name_from_message):
        assert name == name_from_message, f"{name} not equal with {name_from_message}"

    def prices_should_be_equal(self, price, price_from_message):
        assert price == price_from_message, f"{price} not equal with {price_from_message}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADD_TO_BASKET), \
            "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ABOUT_ADD_TO_BASKET), \
            "Should be disappeared"