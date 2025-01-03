import pytest
from helpers.api_client import APIClient
from helpers.validate_response import validate_response
from config.logging_config import logger

@pytest.fixture
def api_client():
    return APIClient()

def test_get_products(api_client):
    response = api_client.get_products()

    products = validate_response(response)

    assert isinstance(products, list), "Response should be a list"
    assert len(products) > 0, "Products list is empty"

    for product in products:
        assert "id" in product, "Product ID is missing"
        assert "title" in product, "Product title is missing"
        assert "price" in product, "Product price is missing"
        assert "category" in product, "Product category is missing"
        assert "description" in product, "Product description is missing"
        assert "image" in product, "Product image is missing"

    logger.info(f"Product data: {products}")