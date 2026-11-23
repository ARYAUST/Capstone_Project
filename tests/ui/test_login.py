from pages.home_page import HomePage
from pages.login_page import LoginPage

from utils.config import BASE_URL
from utils.test_data import (
    VALID_EMAIL,
    VALID_PASSWORD
)


def test_valid_login(page):

    home = HomePage(page)
    login = LoginPage(page)

    home.open_homepage(BASE_URL)

    assert home.is_homepage_loaded()

    login.click_signup_login()

    login.login(
        VALID_EMAIL,
        VALID_PASSWORD
    )

    assert login.verify_login_successful()