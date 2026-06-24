from utils.common_utils import common_utils
from playwright.sync_api import expect
class HomePage:
    def __init__(self, page):
        self.page = page

    def navigate_to_homepage(self):       
        self.page.goto("https://www.amazon.in/", wait_until="domcontentloaded",timeout=10000)
        self.page.screenshot(path="homepage_screenshot1.png", full_page=True)
        continue_btn = self.page.get_by_role("button", name="Continue shopping")
        continue_btn.click()
        self.page.screenshot(path="homepage_screenshot_new1.png", full_page=True)

    def verify_navigation_elements(self):
        print(self.page.url)
        assert self.page.locator("#nav-search").is_visible()
        assert self.page.locator("#twotabsearchtextbox").is_visible()

    def click_category_menu(self):
        self.page.locator("#nav-hamburger-menu").click()
        self.page.wait_for_timeout(2000)  # Wait for the menu to open

    def search_for_product(self, product_name):
        self.page.wait_for_selector("#twotabsearchtextbox")
        self.page.fill("#twotabsearchtextbox", product_name)
        self.page.keyboard.press("Enter")

    def verify_category_page(self):
        assert self.page.locator("#hmenu-content").is_visible()
    def verify_search_results(self):
        assert "mobiles" in self.page.url.lower()   

    def take_screenshot(self, page, filename):
        page.screenshot(path=filename, full_page=True) 

   
        
	
	
	