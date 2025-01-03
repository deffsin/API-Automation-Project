import pytest
from helpers.api_client import APIClient
from helpers.api_helpers import get_sort_results
from helpers.api_helpers import get_products
from config.logging_config import logger

@pytest.fixture
def api_client():
    return APIClient()

def test_get_sort_results(api_client):
    order = "asc" # or 'desc'

    all_products = sorted(get_products(api_client), key=lambda x: x["id"], reverse=False) # if 'desc' then True
    sorted_products = get_sort_results(api_client, value=order)

    assert isinstance(sorted_products, list), "Response should be a list"
    assert len(sorted_products) > 0, "Products list is empty"
    assert all_products == sorted_products, "Products are not sorted correctly"

    for product in sorted_products:
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

    logger.info(f"Product data: {sorted_products}")