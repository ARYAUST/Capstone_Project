from playwright.sync_api import expect
from pages.products_page import ProductsPage


def test_add_product_to_cart(page):
    products = ProductsPage(page)

    page.goto("https://automationexercise.com")
    products.navigate_to_products()
    products.add_product_to_cart()

    expect(page.locator(".modal-content")).to_be_visible(timeout=10000)