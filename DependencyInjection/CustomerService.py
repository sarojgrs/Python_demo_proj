from DependencyInjection.ApiClient import ApiClient
from abc import ABC, abstractmethod


class CustomerService:
    def __init__(self, api_client: ApiClient):
        self.api_client = api_client

    def get_customer_info(self, customer_id: int) -> dict:
        # Call the API client to retrieve customer information
        # You can use the self.api_client instance to interact with the API
        response = self.api_client.get_customer(customer_id)

        # Process the response and return customer information
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Failed to fetch customer information")

    def send_email_notification(self, email: str, message: str) -> None:
        # Call the API client to send an email notification
        # You can use the self.api_client instance to interact with the API
        response = self.api_client.send_email(email, message)

        # Process the response (e.g., log or handle errors)
        if response.status_code != 200:
            print("Failed to send email notification:", response.text)

    def getName(self):
        print("from customerService")
