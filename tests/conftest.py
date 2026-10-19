import pytest

from api.SearchAPI import SearchAPI
from pages.HomePage import HomePage
from pages.ProductDetails import ProductDetails


@pytest.fixture
def home(page):
    return HomePage(page).open()


@pytest.fixture
def product_details(page):
    return ProductDetails(page)

@pytest.fixture
def search_api():
    return SearchAPI()