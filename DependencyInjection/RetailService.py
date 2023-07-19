from DependencyInjection.ApiClient import ApiClient


class RetailService:
    def __init__(self, api_client: ApiClient):
        self.api_client = api_client

    def process_transaction(self, product_id: int, quantity: int) -> None:
        # Call the API client to process the retail transaction
        # You can use the self.api_client instance to interact with the API
        payload = {
            'product_id': product_id,
            'quantity': quantity
        }
        response = self.api_client.process_transaction(payload)

        # Process the response (e.g., log or handle errors)
        if response.status_code != 200:
            print("Failed to process retail transaction:", response.text)
