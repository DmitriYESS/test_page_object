import pytest
from selenium.webdriver.support.ui import WebDriverWait
from .pages.product_page import ProductPage

@pytest.mark.adding_button
def test_can_add_product(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_adding_button()

@pytest.mark.messages
def test_no_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.test_guest_cant_see_success_message_after_adding_product_to_basket()
@pytest.mark.messages
def test_no_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    browser.implicitly_wait(3)
    page = ProductPage(browser, link)
    page.open()
    page.test_guest_cant_see_success_message()

@pytest.mark.messages
def test_success_message_disappeared(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    browser.implicitly_wait(3)
    page = ProductPage(browser, link)
    page.open()
    page.test_message_disappeared_after_adding_product_to_basket()

@pytest.mark.login
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.login
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
