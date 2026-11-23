class HomePage:

    # Locators
    SIGNUP_LOGIN_LINK = "a[href='/login']"
    PRODUCTS_LINK = "a[href='/products']"
    CART_LINK = "a[href='/view_cart']"
    SUBSCRIPTION_EMAIL = "#susbscribe_email"
    SUBSCRIBE_BUTTON = "#subscribe"
    LOGGED_IN_USER = "a:has-text('Logged in as')"

    def __init__(self,page):
        self.page = page

    def open_homepage(self, url):
     self.page.goto(url, wait_until="domcontentloaded", timeout=60000)
     self.page.locator(
        "img[alt='Website for automation practice']"
    ).wait_for(state="visible", timeout=30000)

    def is_homepage_loaded(self):
        return self.page.locator("img[alt='Website for automation practice']").is_visible()