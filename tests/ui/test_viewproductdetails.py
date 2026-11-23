from pages.products_page import ProductsPage


def test_verify_product_cart(page):
    products = ProductsPage(page)

    page.goto("https://automationexercise.com")
    products.navigate_to_products()
    products.add_product_to_cart()
    products.click_continue_shopping()
    products.go_to_cart()

    assert products.verify_product_in_cart()