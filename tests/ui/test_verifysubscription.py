from playwright.sync_api import expect
from pages.home_page import HomePage
from utils.config import BASE_URL


def test_subscription(page):
    home = HomePage(page)

    page.goto(BASE_URL)
    page.locator(home.SUBSCRIPTION_EMAIL).fill("test123@gmail.com")
    page.locator(home.SUBSCRIBE_BUTTON).click()

    expect(
    page.get_by_text("You have been successfully subscribed!", exact=True)
).to_be_visible()