import pytest
from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import sync_playwright
from Pages.HomePage import HomePage

scenarios('../features/Feature/ui.feature')


@pytest.fixture
def home():
    with sync_playwright() as p:    
     browser = p.chromium.launch(headless=True)
     #context = browser.new_context(record_video_dir="videos/")
     #page = context.new_page()
     page = browser.new_page()
     home_page = HomePage(page)
     yield home_page
     #context.close()
     browser.close()

@given('I navigate to the Amazon Home Page')
def navigate_to_home_page(home):
    home.navigate_to_homepage()
    print("Navigated----")


@then('I should see navigation elements')
def verify_navigation_elements(home):
    home.verify_navigation_elements()

@then('I take screenshot of the full Page')
def take_screenshot(home):
    home.take_screenshot(home.page, 'full_page_screenshot.png')

@when('I click on the Category menu')
def click_category_menu(home):
    home.click_category_menu()  

@then('I should be redirect to Categorypage')
def verify_category_page(home):
    home.verify_category_page()

@when('I search for a product')
def search_for_product(home):
    home.search_for_product("mobile")

@then('I should see search results')
def verify_search_results(home):
    home.verify_search_results()