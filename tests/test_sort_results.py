import pytest
from helpers.api_client import APIClient
from helpers.api_helpers import get_sort_results
from helpers.api_helpers import get_products
from config.logging_config import logger

@pytest.fixture
def api_client():
    return APIClient()

def test_get_sort_results(api_client):
    order = "asc" # or 'asc'

    all_products = sorted(get_products(api_client), key=lambda x: x["id"], reverse=False) # if 'desc' then True
    sorted_products = get_sort_results(api_client, value=order)

    assert isinstance(sorted_products, list), "Response should be a list"
    assert len(sorted_products) > 0, "Products list is empty"
    assert all_products == sorted_products, "Products are not sorted correctly"

    for product in sorted_products:
        assert "id" in product, "Product ID is missing"
        assert "title" in product, "Product title is missing"
        assert "price" in product, "Product price is missing"
        assert "category" in product, "Product category is missing"
        assert "description" in product, "Product description is missing"
        assert "image" in product, "Product image is missing"

    logger.info(f"Product data: {sorted_products}")