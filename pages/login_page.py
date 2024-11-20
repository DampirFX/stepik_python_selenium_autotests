from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "login should be in the Url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "registration form is not presented"

    def register_new_user(self, email, password):
        self.input_text_to_field(*LoginPageLocators.FIELD_EMAIL, text=email)
        self.input_text_to_field(*LoginPageLocators.FIELD_PASSWORD, text=password)
        self.input_text_to_field(*LoginPageLocators.FIELD_CONFIRM_PASSWORD, text=password)
        self.click_button(*LoginPageLocators.BUTTON_SUBMIT)
