import pytest
from playwright.sync_api import sync_playwright
from utils.api_utils import APIUtils
from utils.config import Config 

class Context:
    pass

@pytest.fixture()
def context():
    return Context()

@pytest.fixture(scope="session")
def api_utils():
    with sync_playwright() as playwright:
        request_context = playwright.request.new_context(base_url="https://petstore.swagger.io/v2", extra_http_headers={"Content-Type": "application/json", "Accept": "application/json"})
        yield APIUtils(request_context)
        request_context.dispose()

