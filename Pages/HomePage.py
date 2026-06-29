from utils.common_utils import common_utils
from playwright.sync_api import expect

from utils.config import Config
class HomePage:
    def __init__(self, page):
        self.page = page

        #Initializing Locator
        self.continue_btn = page.get_by_role("button", name="Continue shopping")
        self.search_box = page.locator("#twotabsearchtextbox").first
        self.search_bar = page.locator("#nav-bar-left")
        self.hamburger_menu = page.locator("#nav-hamburger-menu")
        self.menu_content = page.locator("#hmenu-content")
        self.first_search_result = page.locator("//div[@data-component-type='s-search-result']").first

    def navigate_to_homepage(self):
        self.page.goto(Config.UI_BASE_URL, wait_until="domcontentloaded", timeout=60000)
        self.page.screenshot(path="homepage.png", full_page=True)
        try:
            if self.continue_btn.is_visible(timeout=5000):
                self.continue_btn.click()
                self.page.screenshot(path="screenshots/HomePage.png", full_page=True)
        except Exception:
            print("Continue button not found, proceeding without clicking it.")       

    def verify_navigation_elements(self):
        expect(self.search_box).to_be_visible(timeout=5000)

    def click_category_menu(self):
        self.hamburger_menu.click()
        self.page.wait_for_timeout(2000) 
        self.page.screenshot(path="screenshots/MenuScreenshot.png", full_page=True)   

    def verify_category_page(self):
        expect(self.menu_content.first).to_be_visible(timeout=5000)
        self.page.screenshot(path="screenshots/CategoryPageScreenshot.png", full_page=True)

    def search_for_product(self):
        self.search_box.wait_for(state="visible")
        self.search_box.fill(Config.SEARCH_PRODUCT)
        self.search_box.press("Enter")
        self.page.screenshot(path="screenshots/MobileSearch.png", full_page=True)

    def verify_search_results(self):
        product_name = self.first_search_result.text_content()
        print("First search result product name:", product_name)
        expect(self.first_search_result).to_be_visible(timeout=5000)

    def take_screenshot(self, page, filename):
        page.screenshot(path=filename, full_page=True) 

   