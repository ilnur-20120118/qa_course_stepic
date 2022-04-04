from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)

    def should_be_an_empty_basket(self):
        """Ожидаем, что в корзине нет товаров"""
        assert self.is_disappeared(*BasketPageLocators.BASKET_FORMSET), \
                "Product in basket"

    def text_cart_is_empty(self):
        """Ожидаем, что есть текст о том что корзина пуста"""
        assert self.is_element_present(*BasketPageLocators.MSG_KARD_IS_EMPTY), \
                       "Отсутствует сообщение о том ,что карта пуста"


