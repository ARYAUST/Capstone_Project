from pages.home_page import HomePage
from pages.signup_page import SignupPage

from utils.config import BASE_URL
from utils.data_generator import DataGenerator


def test_register_new_user(page):

    home = HomePage(page)
    signup = SignupPage(page)

    name = DataGenerator.get_name()
    email = DataGenerator.get_email()

    home.open_homepage(BASE_URL)

    signup.navigate_to_signup()

    signup.enter_signup_details(
        name,
        email
    )

    signup.create_account(
        password="Password123",
        first_name="Arya",
        last_name="Mohan",
        company="UST",
        address="Trivandrum",
        state="Kerala",
        city="Trivandrum",
        zipcode="695001",
        mobile="9999999999"
    )

    assert signup.verify_account_created()