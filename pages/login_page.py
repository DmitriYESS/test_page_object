from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators
from mimesis import Person
from mimesis.locales import Locale

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка на корректный url адрес
        assert 'login' in self.browser.current_url, "Вы не перешли на страницу логина"

    def should_be_login_form(self):
        # проверка, что есть форма логина
        login_form = self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        assert login_form, "Login form is not presented"

    def should_be_register_form(self):
        # проверка что есть форма регистрации на странице
        register_form = self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
        assert register_form, "Register form is not presented"

    def register_new_user(self):
        user_email_generator = Person(locale=Locale.EN).email()
        user_password = Person(locale=Locale.EN).password(length=20)
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(user_email_generator)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD).send_keys(user_password)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_APPROVE).send_keys(user_password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON_LOG_IN).click()
        self.browser.implicitly_wait(10)
        assert self.is_element_present(*LoginPageLocators.SUCCESS), \
                "Success message is not presented, but should be"
