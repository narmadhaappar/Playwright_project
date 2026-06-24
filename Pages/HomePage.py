from utils.common_utils import common_utils


class HomePage:
    def __init__(self, page=None):
        self.page = page
        self.utils = common_utils(self.page)
        self.logo = self.page.locator('a#nav-logo-sprites')
        self.search_box = self.page.locator('input#twotabsearchtextbox')
        self.search_button = self.page.locator('input#nav-search-submit-button')
        self.category_menu = self.page.locator('a#nav-hamburger-menu')

    def navigate_to_homepage(self):
        self.page.goto("https://www.amazon.in/")

    def verify_navigation_elements(self):
        self.utils.is_element_visible(self.logo)
        self.utils.is_element_visible(self.search_box)

    def click_category_menu(self):
        self.utils.click_element(self.category_menu)
        self.utils.click(self.page.locator("text=Mobiles"))

    def search_for_product(self, product_name):
        self.utils.type_text(self.search_box, product_name)
        self.utils.click_element(self.search_button)

    def verify_category_page(self):
        # Add an assertion here for the category page title or header
        self.utils.is_element_visible(self.page.locator('text=Mobiles'))

    def verify_search_results(self):
        # Add an assertion here for search results presence
        self.utils.is_element_visible(self.page.locator('div.s-main-slot'))

   
        
	
	
	