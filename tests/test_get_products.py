import pytest
from helpers.api_client import APIClient

@pytest.fixture
def api_client():
    return APIClient()

def test_get_products(api_client):
    response = api_client.get_products()

    if response.status_code != 200:
        print(f"Unexpected status code: {response.status_code}")
        print(f"Request URL: {response.url}")
        print(f"Response Body: {response.text}")
        pytest.fail(f"Test failed due to unexpected status code: {response.status_code}")

    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"

    products = response.json()

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
