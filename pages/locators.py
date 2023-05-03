from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BASKET_LINK = (By.CSS_SELECTOR, "a[class='btn btn-default']")
    NAME_OF_BOOK_IN_BASKET = (By.CSS_SELECTOR, ".col-sm-4 h3 a")
    NAME_OF_BOOK = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    BOOK_PRISE = (By.CSS_SELECTOR, ".col-sm-6.product_main p.price_color")
    BOOK_PRISE_IN_BASKET = (By.CSS_SELECTOR, ".col-sm-1 p.price_color.align-right")
    HOW_MANY_BOOKS = (By.CSS_SELECTOR, "#id_form-0-quantity, value")
    BOOKS_SUM_PRISE_IN_BASKET = (By.CSS_SELECTOR, ".col-sm-2 p.price_color.align-right")
