import pytest
from helpers.api_client import APIClient
from config.logging_config import logger
from helpers.validate_response import validate_response

@pytest.fixture
def api_client():
    return APIClient()

def test_get_limit_results(api_client):
    response = api_client.get_limit_results(number=2)

    products = validate_response(response)

    assert isinstance(products, list), "Response should be a list"
    assert 1 <= len(products) <= 5, "Products list should contain between 1 and 5 items"

    for product in products:
        assert "id" in product, "Product ID is missing"
        assert "title" in product, "Product title is missing"
        assert "price" in product, "Product price is missing"
        assert "category" in product, "Product category is missing"
        assert "description" in product, "Product description is missing"
        assert "image" in product, "Product image is missing"

    logger.info(f"Product data: {products}")