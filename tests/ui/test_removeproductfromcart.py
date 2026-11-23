from playwright.sync_api import expect
from pages.products_page import ProductsPage


def test_remove_product_from_cart(page):
    products = ProductsPage(page)

    page.goto("https://automationexercise.com")
    products.navigate_to_products()
    products.add_product_to_cart()
    products.click_continue_shopping()
    products.go_to_cart()
    products.remove_product_from_cart()

    expect(page.locator("#product-1")).to_have_count(0)