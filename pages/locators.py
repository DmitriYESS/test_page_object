from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a.btn-default")
    NAME_OF_BOOK_IN_BASKET = (By.CSS_SELECTOR, ".col-sm-4 h3 a")
    NAME_OF_BOOK_IN_LINE = (By.CSS_SELECTOR, "#messages div:nth-child(1) div strong")
    NAME_OF_BOOK = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    BOOK_PRISE = (By.CSS_SELECTOR, ".col-sm-6.product_main p.price_color")
    BOOK_PRISE_IN_BASKET = (By.CSS_SELECTOR, ".col-sm-1 p.price_color.align-right")
    BOOK_PRISE_IN_LINE = (By.CSS_SELECTOR, ".alertinner p strong")
    HOW_MANY_BOOKS = (By.CSS_SELECTOR, "#id_form-0-quantity, value")
    BOOKS_SUM_PRISE_IN_BASKET = (By.CSS_SELECTOR, ".col-sm-2 p.price_color.align-right")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")