from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject
from DependencyInjection.ApiClient import ApiClient
from DependencyInjection.CustomerService import CustomerService
from DependencyInjection.RetailService import RetailService


class Container(containers.DeclarativeContainer):

    config = providers.Configuration()

    api_client = providers.Singleton(
        ApiClient,
        api_key=config.api_key,
        timeout=config.timeout,
    )

    customer_service = providers.Factory(
        CustomerService,
        api_client=api_client,
    )

    retail_service = providers.Factory(
        RetailService,
        api_client=api_client,
    )


@inject
def main(
    customer_service: CustomerService = Provide[Container.customer_service],
    retail_service: RetailService = Provide[Container.retail_service]
) -> None:
    # Use customer_service and retail_service as needed

    # Example 1: Get customer information
    # customer_id = 123
    # customer_info = customer_service.get_customer_info(customer_id)
    # # customer_info = customer_service.getName()
    # print("Customer Information:", customer_info)

    # # Example 2: Process a retail transaction
    # product_id = 456
    # quantity = 2
    # retail_service.process_transaction(product_id, quantity)
    # print("Retail transaction processed successfully")

    # # Example 3: Call a shared method between services
    # customer_service.send_email_notification(
    #     "example@example.com", "Hello, customer!")

    # Other code logic...
    print('test')


if __name__ == "__main__":
    container = Container()
    container.config.api_key.from_env("API_KEY", required=True)
    container.config.timeout.from_env("TIMEOUT", as_=int, default=5)
    container.wire(modules=[__name__])

    main()  # <-- dependencies are injected automatically
