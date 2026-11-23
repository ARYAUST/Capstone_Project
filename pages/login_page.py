from playwright.sync_api import Page


class LoginPage:

    signup_login_link = "a[href='/login']"

    email_input = "[data-qa='login-email']"
    password_input = "[data-qa='login-password']"

    login_button = "[data-qa='login-button']"
    logout_button = "a[href='/logout']"

    logged_in_as = "text=Logged in as"

    error_message = "text=Your email or password is incorrect!"

    def __init__(self, page: Page):
        self.page = page

    def click_signup_login(self):
        self.page.click(self.signup_login_link)

    def login(self, email, password):
        self.page.fill(self.email_input, email)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)
        self.page.wait_for_timeout(3000)
        self.page.screenshot(path="login_result.png")

    def verify_login_successful(self):
        return self.page.locator(
            self.logged_in_as
        ).is_visible()

    def verify_login_failed(self):
        return self.page.locator(
            self.error_message
        ).is_visible()

    def get_email_validation_message(self):
     return self.page.locator(
        "[data-qa='login-email']"
    ).evaluate(
        "element => element.validationMessage"
    )

    def click_logout(self):
        self.page.click(self.logout_button)
        self.page.wait_for_timeout(3000)

    def verify_logout_successful(self):
        return "/login" in self.page.url