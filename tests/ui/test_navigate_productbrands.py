from pages.products_page import ProductsPage


def test_navigate_brands(page):
    products = ProductsPage(page)

    page.goto("https://automationexercise.com")
    products.navigate_to_products()
    products.select_polo_brand()

    assert products.verify_brand_page()