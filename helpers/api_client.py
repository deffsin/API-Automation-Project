import requests
from config.settings import BASE_URL

class APIClient:
    def __init__(self):
        self.base_url = BASE_URL
        self.session = requests.Session()

    def get_products(self):
        url = f"{self.base_url}/products"
        response = self.session.get(url)
        print(f"Request URL: {url}, Response Status: {response.status_code}, Response Body: {response.text}")
        return response