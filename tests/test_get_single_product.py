import pytest
from helpers.api_client import APIClient
from helpers.api_helpers import get_single_product
from helpers.api_helpers import get_products
from config.logging_config import logger

@pytest.fixture
def api_client():
    return APIClient()

def test_get_single_product(api_client):
    products = get_products(api_client)
    product = get_single_product(api_client, 2)

    assert isinstance(product, dict), "Response should be a dictionary"
    assert product in products, "The product isn't found in the list"

    for product in products:
        assert "id" in product, "Product ID is missing"
        assert isinstance(product["id"], int), f"Product ID is not an integer: {product['id']}"

        assert "title" in product, "Product title is missing"
        assert isinstance(product["title"], str), f"Product title is not a string: {product['title']}"

        assert "price" in product, "Product price is missing"
        assert isinstance(product["price"], (int, float)), f"Product price is not an integer or float: {product['price']}"

        assert "category" in product, "Product category is missing"
        assert isinstance(product["category"], str), f"Product price is not a string: {product['category']}"

        assert "description" in product, "Product description is missing"
        assert isinstance(product["description"], str), f"Product description is not a string: {product['description']}"

        assert "image" in product, "Product image is missing"
        assert isinstance(product["image"], str), f"Product image is not a string: {product['image']}"

    logger.info(f"Product data: {product}")
