import pytest
from helpers.api_client import APIClient
from helpers.api_helpers import get_products
from config.logging_config import logger

@pytest.fixture
def api_client():
    return APIClient()

def test_get_products(api_client):
    products = get_products(api_client)

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