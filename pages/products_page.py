from playwright.sync_api import Page


class ProductsPage:

    products_link = "a[href='/products']"

    products_page_title = "text=All Products"

    search_input = "#search_product"
    search_button = "#submit_search"

    first_view_product = "a[href='/product_details/1']"

    add_to_cart_button = "a[data-product-id='1']"

    continue_shopping = "button.btn.btn-success"

    cart_link = "a[href='/view_cart']"

    product_in_cart = "#product-1"
    cart_product_name = "#product-1 .cart_description h4 a"
    cart_quantity = "#product-1 .cart_quantity button"

    delete_product = ".cart_quantity_delete"

    women_category = "a[href='#Women']"
    women_dress = "a[href='/category_products/1']"

    brand_polo = "a[href='/brand_products/Polo']"

    def __init__(self, page: Page):
        self.page = page

    def navigate_to_products(self):
        self.page.click(self.products_link)

    def verify_products_page(self):
        return self.page.locator(
            self.products_page_title
        ).is_visible()

    def search_product(self, product_name):
        self.page.fill(
            self.search_input,
            product_name
        )
        self.page.click(
            self.search_button
        )

    def verify_search_results(self, product_name):
        return self.page.locator(
            f"text={product_name}"
        ).first.is_visible()

    def view_first_product(self):
        self.page.click(
            self.first_view_product
        )

    def verify_cart_product_exists(self):
        return self.page.locator(self.product_in_cart).count() > 0

    
    def verify_product_detail_page(self):
        return "/product_details/" in self.page.url

    def get_cart_product_name(self):
        return self.page.locator(self.cart_product_name).inner_text()

    def get_cart_quantity(self):
        return self.page.locator(self.cart_quantity).inner_text()

    def add_product_to_cart(self):
        self.page.hover(
            ".single-products"
        )
        self.page.click(
            self.add_to_cart_button
        )

    def click_continue_shopping(self):
        self.page.click(
            self.continue_shopping
        )

    def go_to_cart(self):
        self.page.click(
            self.cart_link
        )

    def verify_product_in_cart(self):
        return self.page.locator(
            self.product_in_cart
        ).is_visible()

    def remove_product_from_cart(self):
        self.page.click(
            self.delete_product
        )

    def select_women_category(self):
        self.page.click(
            self.women_category
        )
        self.page.click(
            self.women_dress
        )

    def verify_category_page(self):
        return "/category_products/" in self.page.url

    def select_polo_brand(self):
        self.page.click(
            self.brand_polo
        )

    def verify_brand_page(self):
        return "/brand_products/" in self.page.url 