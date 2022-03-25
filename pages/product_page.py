from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_shoping_cart(self):
        assert self.is_element_present(*ProductPageLocators.ADD_CARD), "cart botton not found"
        card_link = self.browser.find_element(*ProductPageLocators.ADD_CARD)
        card_link.click()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MSG_ADD_PRODUCT), """
        Появилось сообщение о добавлении продукта, так не должно быть!
        """

    def should_not_disappear_msg(self):
        x = self.is_disappeared(*ProductPageLocators.MSG_ADD_PRODUCT), "Должен был исчезнуть, но не исчез"
        assert (x != False), "Сообщение по какой то причине исчезло"

    def should_disappear_msg(self):
        assert self.is_disappeared(*ProductPageLocators.MSG_ADD_PRODUCT), \
        ("Сообщение должно исчезуть, но не исчезло")

    def examination_correct_msg(self):
        """ Сообщение о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром,
            который вы действительно добавили.
        """
        name_product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        msg_about_product_add_in_basket = self.browser.find_element(*ProductPageLocators.MSG_ADD_PRODUCT).text
        assert name_product == msg_about_product_add_in_basket, "название продукта не совпадает или что-то еще"

    def examination_correct_price_in_basket(self):
        """ Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара.
        """
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        price_card = self.browser.find_element(*ProductPageLocators.PRICE_CARD).text
        assert price_product in price_card, "цена продукта не соответствует цене в карзине"


