from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_adding_button(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        assert add_button, "Add button is not presented"
        add_button.click()
        self.solve_quiz_and_get_code()

