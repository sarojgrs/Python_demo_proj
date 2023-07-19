from starlette.requests import Request
from starlette.responses import PlainTextResponse, JSONResponse
from starlette.endpoints import HTTPEndpoint
from starlette.routing import Route
from starlette.types import Receive, Scope, Send
from Controller.Base import BaseController
from DependencyInjection.ApiClient import ApiClient
from DependencyInjection.CustomerService import CustomerService
from DesignPattern.FactoryMethodDesignPattern import MainClass
from DesignPattern.SingletonDesignPattern import Singleton
from DesignPattern.FactoryMethodDesignPatternFileProcess import FactoryMethodImplementation


class UserController(BaseController):

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    # @staticmethod
    # @property

    def __init__(self, api_client: ApiClient, customer_service: CustomerService):
        self.api_client = api_client
        self.customer_service = customer_service

    async def get(self, request: Request):
        # username = request.path_params['username']
        a = self.customer_service.get_customer_info(232)
        # address = request.query_params['address']
        # return PlainTextResponse('hello, %s!' % username)
        return PlainTextResponse('hello, %s!')

    @classmethod
    async def getname(self, request: Request):
        username = request.path_params['username']
        # address = request.query_params['address']
        return PlainTextResponse('hello, %s!' % username)

    @classmethod
    async def list_users(cls, request):
        # Logic to list users
        # return JSONResponse({"users": [...]})
        # ob = MainClass()
        # ob.dogWala
        # ob = Singleton.get_instance()
        # return PlainTextResponse('hello, %s!')

        # Create an instance of the class calling DI services..
        instance = cls(ApiClient, CustomerService)
        result = instance.customer_service.get_customer_info(cls, 2)

        ob = FactoryMethodImplementation()
        result = list(ob.run())

        return PlainTextResponse('hello, %s! ' % result)
