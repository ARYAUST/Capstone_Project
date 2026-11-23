import pytest
from playwright.sync_api import sync_playwright
from api.api_client import AutomationExerciseAPI


@pytest.fixture
def api():
    return AutomationExerciseAPI()

@pytest.fixture
def page():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        yield page

        browser.close()