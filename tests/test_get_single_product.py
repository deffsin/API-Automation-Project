import pytest
from helpers.api_client import APIClient
from config.logging_config import logger
from helpers.validate_response import validate_response

@pytest.fixture
def api_client():
    return APIClient()

def test_get_single_product(api_client):
    response = api_client.get_single_product()

    product = validate_response(response)

    assert isinstance(product, dict), "Response should be a dictionary"
    assert "id" in product, "Product ID is missing"
    assert "title" in product, "Product title is missing"
    assert "price" in product, "Product price is missing"
    assert "category" in product, "Product category is missing"
    assert "description" in product, "Product description is missing"
    assert "image" in product, "Product image is missing"

    logger.info(f"Product data: {product}")
