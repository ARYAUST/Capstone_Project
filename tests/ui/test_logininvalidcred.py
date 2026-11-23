from pages.home_page import HomePage
from pages.login_page import LoginPage

from utils.config import BASE_URL
from utils.test_data import (
    INVALID_EMAIL,
    INVALID_PASSWORD
)


def test_invalid_login(page):

    home = HomePage(page)
    login = LoginPage(page)

    home.open_homepage(BASE_URL)

    login.click_signup_login()

    login.login(
        INVALID_EMAIL,
        INVALID_PASSWORD
    )

    assert login.verify_login_failed()