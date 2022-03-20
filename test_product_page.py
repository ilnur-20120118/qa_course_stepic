from .pages.product_page import ProductPage
import time
import pytest


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
     pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"{link}"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_shoping_cart()
    product_page.solve_quiz_and_get_code()
    product_page.examination_correct_msg()
    product_page.examination_correct_price_in_basket()



"""
Измените методы проверки таким образом, чтобы они принимали как аргумент название товара и цену товара.
Сделайте метод, который вытаскивает из элемента текст-название товара и возвращает его.
Сделайте такой же метод для цены.
Теперь проверяйте, что название товара в сообщении совпадает с заголовком товара.
"""

