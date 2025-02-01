import pytest
from helpers.api_client import APIClient
from helpers.api_helpers import get_in_category
from config.logging_config import logger

@pytest.fixture
def api_client():
    return APIClient()

def test_get_in_category(api_client):
    category_name = "jewelery"
    products = get_in_category(api_client, category_name=category_name)
    print(type(products))

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

    logger.info(f"Product data: {products}")