

from pages.products_page import ProductsPage


def test_verify_product_in_cart(page):
    products = ProductsPage(page)

    page.goto("https://automationexercise.com")
    products.navigate_to_products()
    products.add_product_to_cart()
    products.click_continue_shopping()
    products.go_to_cart()

    product_name = products.get_cart_product_name()
    quantity = products.get_cart_quantity()

    assert product_name is not None
    assert quantity == "1"