import time
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import InvalidSelectorException


class ProductPage(BasePage):
    def should_be_adding_button(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        assert add_button, "Add button is not presented"
        add_button.click()
        self.solve_quiz_and_get_code()
        name = self.browser.find_element(*ProductPageLocators.NAME_OF_BOOK).text
        print(name)
        price = self.browser.find_element(*ProductPageLocators.BOOK_PRISE).text
        print(price)
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_LINK)
        time.sleep(3)
        assert basket_button, "Add button is not presented"
        basket_button.click()
        time.sleep(2)
        name_in_basket = self.browser.find_element(*ProductPageLocators.NAME_OF_BOOK_IN_BASKET).text
        print(name_in_basket)
        price_in_basket = self.browser.find_element(*ProductPageLocators.BOOK_PRISE_IN_BASKET).text
        print(price_in_basket)
        sum_in_basket = self.browser.find_element(*ProductPageLocators.BOOKS_SUM_PRISE_IN_BASKET).text
        print(sum_in_basket)
        self.name_in_busket_should_be_name(name, name_in_basket)
        self.price_in_busket_should_be_price(price, price_in_basket)
        self.sum_in_busket_should_be_sum(price, sum_in_basket)

    def name_in_busket_should_be_name(self, name, name_in_basket):
        try:
            assert name_in_basket == name, "Incorrect book"
            print("correct name "+name)
        except InvalidSelectorException:
            print('NAME?')

    def price_in_busket_should_be_price(self, price, price_in_basket):
        try:
            assert price_in_basket == price, "Incorrect price"
            print("correct price " + price)
        except InvalidSelectorException:
            print('PRICE?')

    def sum_in_busket_should_be_sum(self, sum, sum_in_basket):
        try:
            assert sum_in_basket == sum, "Incorrect sum"
            print("correct sum " + sum)
        except InvalidSelectorException:
            print('SUM?')
