# utils/helper.py

class Helper:

    @staticmethod
    def wait_for_element(page, locator):
        page.locator(locator).wait_for()

    @staticmethod
    def get_page_title(page):
        return page.title()

    @staticmethod
    def scroll_to_bottom(page):
        page.evaluate(
            "window.scrollTo(0, document.body.scrollHeight)"
        )