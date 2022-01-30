import pytest
from .pages.product_page import ProductPage

base_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer"


@pytest.mark.parametrize('offer_number', ["0", "1", "2", "3", "4", "5", "6",
                                          pytest.param("7", marks=pytest.mark.xfail),
                                          "8", "9"])
def test_guest_can_add_product_to_basket(browser, offer_number):
    product_link = base_link+offer_number
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_add_to_basket_notification()
    product_page.product_name_is_correct_in_notification()
    product_page.should_be_your_basket_total_notification()
    product_page.basket_price_is_equal_to_product_price()
