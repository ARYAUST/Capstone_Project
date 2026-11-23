from playwright.sync_api import Page


class SignupPage:

    # Login / Signup page locators
    SIGNUP_LOGIN_LINK = "a[href='/login']"
    SIGNUP_NAME = "[data-qa='signup-name']"
    SIGNUP_EMAIL = "[data-qa='signup-email']"
    SIGNUP_BUTTON = "[data-qa='signup-button']"

    # Account Information
    TITLE_MR = "#id_gender1"
    PASSWORD = "[data-qa='password']"

    DAY = "[data-qa='days']"
    MONTH = "[data-qa='months']"
    YEAR = "[data-qa='years']"

    FIRST_NAME = "[data-qa='first_name']"
    LAST_NAME = "[data-qa='last_name']"
    COMPANY = "[data-qa='company']"
    ADDRESS1 = "[data-qa='address']"
    COUNTRY = "[data-qa='country']"
    STATE = "[data-qa='state']"
    CITY = "[data-qa='city']"
    ZIPCODE = "[data-qa='zipcode']"
    MOBILE_NUMBER = "[data-qa='mobile_number']"

    CREATE_ACCOUNT = "[data-qa='create-account']"

    ACCOUNT_CREATED = "text=Account Created!"

    def __init__(self, page: Page):
        self.page = page

    def navigate_to_signup(self):
        self.page.click(self.SIGNUP_LOGIN_LINK)

    def enter_signup_details(self, name, email):
        self.page.fill(self.SIGNUP_NAME, name)
        self.page.fill(self.SIGNUP_EMAIL, email)
        self.page.click(self.SIGNUP_BUTTON)

    def create_account(
        self,
        password,
        first_name,
        last_name,
        company,
        address,
        state,
        city,
        zipcode,
        mobile
    ):

        self.page.check(self.TITLE_MR)

        self.page.fill(self.PASSWORD, password)

        self.page.select_option(self.DAY, "10")
        self.page.select_option(self.MONTH, "5")
        self.page.select_option(self.YEAR, "1995")

        self.page.fill(self.FIRST_NAME, first_name)
        self.page.fill(self.LAST_NAME, last_name)
        self.page.fill(self.COMPANY, company)
        self.page.fill(self.ADDRESS1, address)

        self.page.select_option(
            self.COUNTRY,
            "India"
        )

        self.page.fill(self.STATE, state)
        self.page.fill(self.CITY, city)
        self.page.fill(self.ZIPCODE, zipcode)
        self.page.fill(self.MOBILE_NUMBER, mobile)

        self.page.click(self.CREATE_ACCOUNT)

    def verify_account_created(self):
        return self.page.locator(
            self.ACCOUNT_CREATED
        ).is_visible()