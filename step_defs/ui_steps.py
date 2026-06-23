from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import sync_playwright
from Pages.HomePage import HomePage

scenarios('../features/ui.feature/ui.feature')

@given('the user is on the homepage')
def launch_AmazonPage():
    global page, browser, home

    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    home = HomePage(page)
    home.navigate_to_homepage()

@then('Then I should see navigation elements')
def verify_navigation_elements():
    home.verify_navigation_elements()

@then('I take screenshot of the full Page')
def take_screenshot():
    home.utils.take_screenshot(page, 'full_page_screenshot.png')

@when('I click on the Category menu')
def click_category_menu():
    home.click_category_menu()  

@then('Then I should be redirect to Categorypage')
def verify_category_page():
    home.verify_category_page()

@when('I Search for the product "mobiles"')
def search_for_product():
    home.search_for_product("mobiles")

@then('I should see search results')
def verify_search_results():
    home.verify_search_results()