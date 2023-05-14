import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    @pytest.mark.login
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        browser.implicitly_wait(3)
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user()

    @pytest.mark.login
    def test_no_success_message_user(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        browser.implicitly_wait(3)
        page = ProductPage(browser, link)
        page.open()
        page.test_guest_cant_see_success_message()

    @pytest.mark.login
    def test_user_can_add_product(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_adding_button()

@pytest.mark.messages
def test_no_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    browser.implicitly_wait(3)
    page = ProductPage(browser, link)
    page.open()
    page.test_guest_cant_see_success_message()

@pytest.mark.adding_button
def test_can_add_product(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
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

#@pytest.mark.login
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

#@pytest.mark.login
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
