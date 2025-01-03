import requests
from config.settings import BASE_URL

class APIClient:
    def __init__(self):
        self.base_url = BASE_URL
        self.session = requests.Session()

    def get_products(self):
        url = f"{self.base_url}/products"
        response = self.session.get(url)
        print(f"Request URL: {url}, Response Status: {response.status_code}")
        return response

    def get_single_product(self, id):
        url = f"{self.base_url}/products/{id}"
        response = self.session.get(url)
        print(f"Request URL: {url}, Response Status: {response.status_code}")
        return response

    def get_limit_results(self, value):
        url = f"{self.base_url}/products?limit={value}"
        response = self.session.get(url)
        print(f"Request URL: {url}, Response Status: {response.status_code}")
        return response

    def sort_results(self, value):
        url = f"{self.base_url}/products?sort={value}"
        response = self.session.get(url)
        print(f"Request URL: {url}, Response Status: {response.status_code}")
        return response