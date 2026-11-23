from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.config import BASE_URL


def test_login_with_empty_fields(page):

    home = HomePage(page)
    login = LoginPage(page)

    home.open_homepage(BASE_URL)

    login.click_signup_login()

    login.login("", "")

    # Verify user is not logged in
    assert not login.verify_login_successful()