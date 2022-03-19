from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link ="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_shoping_cart()
    product_page.solve_quiz_and_get_code()
    time.sleep(15)
    product_page.examination_correct_msg()
    product_page.examination_correct_price_in_basket()

