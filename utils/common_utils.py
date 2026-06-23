from playwright.sync_api import Page, expect

class common_utils:
    def __init__(self, page: Page):
        self.page = page

    def take_screenshot(self, page: Page, filename: str):
        page.screenshot(path=filename)

    def is_element_visible(self, element):
        expect(element).to_be_visible()

    def click_element(self, element):
        element.click()

    def type_text(self, element, text):
        element.type(text)

    def wait_for_element(self, selector: str, timeout: int = 5000):
        self.page.wait_for_selector(selector, timeout=timeout)