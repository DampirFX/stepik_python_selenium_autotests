from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_message_about_empty_basket(self):
        assert (self.get_text_from_element(*BasketPageLocators.MESSAGE_EMPTY_BASKET) ==
                "Your basket is empty. Continue shopping"), "Basket is not empty"

    def should_not_be_items_in_the_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_IN_THE_BASKET), \
            "Items is presented, but should not be"