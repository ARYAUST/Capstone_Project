import requests
from api.endpoints import *



class AutomationExerciseAPI:

    def get_all_products(self):
        return requests.get(
            f"{self.base_url}{PRODUCTS_LIST}",
            verify=False
        )

    def __init__(self):
        self.base_url = BASE_URL

    def get_all_brands(self):
        return requests.get(
            f"{self.base_url}{BRANDS_LIST}",
            verify=False
        )

    def search_product(self, product_name):
        payload = {
            "search_product": product_name
        }

        return requests.post(
            f"{self.base_url}{SEARCH_PRODUCT}",
            data=payload,
            verify=False
        )

    def verify_login(self, email, password):
        payload = {
            "email": email,
            "password": password
        }

        return requests.post(
            f"{self.base_url}{VERIFY_LOGIN}",
            data=payload,
            verify=False
        )

    def create_account(self, user_data):
        return requests.post(
            f"{self.base_url}{CREATE_ACCOUNT}",
            data=user_data,
            verify=False
        )

    def update_account(self, user_data):
        return requests.put(
            f"{self.base_url}{UPDATE_ACCOUNT}",
            data=user_data,
            verify=False
        )

    def delete_account(self, email, password):
        payload = {
            "email": email,
            "password": password
        }

        return requests.delete(
            f"{self.base_url}{DELETE_ACCOUNT}",
            data=payload,
            verify=False
        )

    def get_user_details(self, email):
        return requests.get(
            f"{self.base_url}{GET_USER_DETAILS}",
            params={"email": email},
            verify=False
        )