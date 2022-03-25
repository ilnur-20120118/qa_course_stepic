from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR,"#register_form")


class ProductPageLocators():
    ADD_CARD = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MSG_ADD_PRODUCT = (By.CSS_SELECTOR, "div.alertinner strong")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "div.product_main p.price_color")
    PRICE_CARD = (By.CSS_SELECTOR, "div.basket-mini")
