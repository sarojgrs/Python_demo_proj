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
from dependency_injector.wiring import Provide, inject
from DependencyInjection.withService import Container
from DependencyInjection.CustomerService import CustomerService
from dependency_injector.wiring import inject, Provide


@inject
class Abc(HTTPEndpoint):
 # def __init__(self,  customer_service: CustomerService = Provide[Container.customer_service]):
    #     self.customer_service = customer_service
    # def __init__(self, customer_service: CustomerService):
    #     self.customer_service = customer_service

    def __init__(self):
        self.customer_service = Provide[Container.customer_service]

    async def get(self, request: Request):
        a = self.customer_service.get_customer_info(333)
        return PlainTextResponse('hello from abc')

    async def getName(self):
        customer_service = Provide[Container.customer_service]
        a = customer_service.get_customer_info(333)
        return PlainTextResponse('hello, I got the name')
