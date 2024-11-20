from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import pytest
from .pages.login_page import LoginPage


promo_links_list = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]

# @pytest.mark.parametrize('link', promo_links_list)
def test_guest_can_add_product_to_basket(browser, link):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    name = page.get_product_name()
    price = page.get_product_price()
    page.should_be_present_button_add_to_basket()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_present_message_about_adding_to_basket()
    page.should_be_present_message_about_basket_total()
    name_from_message = page.get_product_name_from_message()
    price_from_message = page.get_product_price_from_message()
    page.names_should_be_equal(name, name_from_message)
    page.prices_should_be_equal(price, price_from_message)
    print()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items_in_the_basket()
    basket_page.should_be_message_about_empty_basket()