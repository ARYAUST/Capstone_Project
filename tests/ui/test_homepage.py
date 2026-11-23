from pages.home_page import HomePage
from utils.config import BASE_URL


def test_homepage_load(page):

    home = HomePage(page)

    home.open_homepage(BASE_URL)

    assert home.is_homepage_loaded()