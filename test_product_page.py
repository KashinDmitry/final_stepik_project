from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_add_to_basket_notification()
    product_page.product_name_is_correct_in_notification()
    product_page.should_be_your_basket_total_notification()
    product_page.basket_price_is_equal_to_product_price()
