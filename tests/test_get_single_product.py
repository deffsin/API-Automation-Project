import pytest
from helpers.api_client import APIClient
from config.logging_config import logger


@pytest.fixture
def api_client():
    return APIClient()

def test_get_single_product(api_client):
    response = api_client.get_single_product()

    if response.status_code != 200:
        logger.error(f"Unexpected status code: {response.status_code}")
        logger.error(f"Request URL: {response.url}")
        logger.error(f"Response Body: {response.text}")
        pytest.fail(f"Test failed due to unexpected status code: {response.status_code}")

    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"

    product = response.json()

    assert isinstance(product, dict), "Response should be a dictionary"
    assert "id" in product, "Product ID is missing"
    assert "title" in product, "Product title is missing"
    assert "price" in product, "Product price is missing"
    assert "category" in product, "Product category is missing"
    assert "description" in product, "Product description is missing"
    assert "image" in product, "Product image is missing"

    logger.info(f"Product data: {product}")
