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
        self.browser.implicitly_wait(5)
        name = self.browser.find_element(*ProductPageLocators.NAME_OF_BOOK).text
        name_in_line = self.browser.find_element(*ProductPageLocators.NAME_OF_BOOK_IN_LINE).text
        price = self.browser.find_element(*ProductPageLocators.BOOK_PRISE).text
        price_in_line = self.browser.find_element(*ProductPageLocators.BOOK_PRISE_IN_LINE).text
        self.name_in_busket_should_be_name(name, name_in_line)
        self.price_in_busket_should_be_price(price, price_in_line)

    def test_guest_cant_see_success_message_after_adding_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        assert add_button, "Add button is not presented"
        add_button.click()
        self.should_not_be_success_message()

    def test_guest_cant_see_success_message(self):
        self.should_not_be_success_message()

    def test_message_disappeared_after_adding_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        assert add_button, "Add button is not presented"
        add_button.click()
        self.success_message_is_disappeared()

    def name_in_busket_should_be_name(self, name, name_in_line):
        try:
            assert name == name_in_line, f"Incorrect book {name_in_line}"
            print(f"correct name {name}")
        except InvalidSelectorException:
            print('NAME?')

    def price_in_busket_should_be_price(self, price, price_in_line):
        try:
            assert price == price_in_line, f"Incorrect price {price_in_line}"
            print(f"correct price {price}")
        except InvalidSelectorException:
            print('PRICE?')

    def sum_in_busket_should_be_sum(self, sum, sum_in_basket):
        try:
            assert sum_in_basket == sum, "Incorrect sum"
            print(f"correct sum {sum}")
        except InvalidSelectorException:
            print('SUM?')

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"
