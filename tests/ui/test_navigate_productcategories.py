

from pages.products_page import ProductsPage


def test_navigate_categories(page):
    products = ProductsPage(page)

    page.goto("https://automationexercise.com")
    products.navigate_to_products()
    products.select_women_category()

    assert products.verify_category_page()