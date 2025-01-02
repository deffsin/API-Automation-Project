import pytest
from helpers.api_client import APIClient
from helpers.validate_response import validate_response

@pytest.fixture
def api_client():
    return APIClient()

def test_get_products(api_client):
    response = api_client.get_products()

    products = validate_response(response)

    assert isinstance(products, list), "Response should be a list"
    assert len(products) > 0, "Products list is empty"

    first_product = products[0]
    assert "id" in first_product, "Product ID is missing"
    assert "title" in first_product, "Product title is missing"
    assert "price" in first_product, "Product price is missing"
    assert "category" in first_product, "Product category is missing"
    assert "description" in first_product, "Product description is missing"
    assert "image" in first_product, "Product image is missing"

    # output for debugging
    print("First product:", first_product)
