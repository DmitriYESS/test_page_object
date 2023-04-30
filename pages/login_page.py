from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка на корректный url адрес
        correct_url = self.browser.support.expected_conditions.url_contains(self.browser.current_url, 'login')
        assert correct_url, "Вы не перешли на страницу логина"

    def should_be_login_form(self):
        # проверка, что есть форма логина
        login_form = self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        assert login_form, "Login link is not presented"

    def should_be_register_form(self):
        # проверка что есть форма регистрации на странице
        register_form = self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
        assert register_form, "Login link is not presented"
