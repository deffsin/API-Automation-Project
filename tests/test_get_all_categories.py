import pytest
from helpers.api_client import APIClient
from helpers.api_helpers import get_all_categories
from config.logging_config import logger

@pytest.fixture
def api_client():
    return APIClient()

def test_get_all_categories(api_client):
    categories = get_all_categories(api_client)

    assert isinstance(categories, list), "Response should be a list"

    for category in categories:
        assert isinstance(category, str), f"Category is not a string: {category}"

    logger.info(f"Categories data: {categories}")