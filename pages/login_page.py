from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        try:
            login_url = self.browser.current_url
            if "login" in login_url:
                assert True
            else:
                assert False, "login not in login_url"
        except Exception:
            assert False, "Error, хз что пошло не так"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "not login form"


    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "not register form"

    def register_new_user(self, email, password):
        """ принимает две строки и регистрирует пользователя"""
        self.email = email
        self.password = password
        self.email_reg = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT_REG)
        self.email_reg.send_keys(self.email)
        self.password1_reg = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT_REG)
        self.password1_reg.send_keys(self.password)
        self.password2_reg = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT_TWO_REG)
        self.password2_reg.send_keys(self.password)
        self.btn = self.browser.find_element(*LoginPageLocators.BTN_REGISTER_FORM)
        self.btn.click()



"""
    EMAIL_INPUT_REG = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_INPUT_REG = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_INPUT_TWO_REG = (By.CSS_SELECTOR, "#id_registration-password2")
    BTN_REGISTER_FORM = (By.CSS_SELECTORbutton[name=registration_submit]")

     price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).tex
     """

  
