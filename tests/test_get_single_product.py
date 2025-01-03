import pytest
from helpers.api_client import APIClient
from helpers.api_helpers import get_single_product
from config.logging_config import logger

@pytest.fixture
def api_client():
    return APIClient()

def test_get_single_product(api_client):
    product = get_single_product(api_client, 2)

    assert isinstance(product, dict), "Response should be a dictionary"

    assert "id" in product, "Product ID is missing"
    assert "title" in product, "Product title is missing"
    assert "price" in product, "Product price is missing"
    assert "category" in product, "Product category is missing"
    assert "description" in product, "Product description is missing"
    assert "image" in product, "Product image is missing"

    logger.info(f"Product data: {product}")
