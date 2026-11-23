from pages.products_page import ProductsPage

def test_navigate_products(page):
    products = ProductsPage(page)

    page.goto("https://automationexercise.com")
    products.navigate_to_products()
    def wait_for_products_page_to_load():
        ...

    wait_for_products_page_to_load()
    

    assert "products" in page.url.lower()