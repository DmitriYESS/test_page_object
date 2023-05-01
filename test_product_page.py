from .pages.product_page import ProductPage
from .pages.base_page import BasePage

link= "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear)"


def test_can_add_product(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_adding_button()

