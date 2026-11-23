from pages.products_page import ProductsPage


def test_search_product(page):
    products = ProductsPage(page)

    page.goto("https://automationexercise.com")
    products.navigate_to_products()
    products.search_product("Blue Top")

    assert products.verify_search_results("Blue Top")


def test_view_product_details(page):
    products = ProductsPage(page)

    page.goto("https://automationexercise.com")
    products.navigate_to_products()
    products.view_first_product()

    assert products.verify_product_detail_page()