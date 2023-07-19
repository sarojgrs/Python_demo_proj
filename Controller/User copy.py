from starlette.requests import Request
from starlette.responses import PlainTextResponse, JSONResponse
from starlette.endpoints import HTTPEndpoint
from starlette.routing import Route
from Controller.Base import BaseController
from DependencyInjection.CustomerService import CustomerService
from DependencyInjection.withService import Container


class UserController1(BaseController):
    customer_service = Container
    # def __init__(self, scope, receive, send):
    #     self.scope = scope
    #     self.receive = receive
    #     self.send = send
    # super().__init__(scope=scope, receive=receive, send=send)
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    def __init__(self, customer_service: CustomerService, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.customer_service = customer_service
    # @staticmethod
    # @property

    async def get(self, request: Request):
        username = request.path_params['username']
        # address = request.query_params['address']
        return PlainTextResponse('hello, %s!' % username)

    @classmethod
    async def getname(self, request: Request):
        username = request.path_params['username']
        # address = request.query_params['address']
        return PlainTextResponse('hello, %s!' % username)

    @classmethod
    async def list_users(self, request):
        # Logic to list users
        # return JSONResponse({"users": [...]})
        name = self.customer_service.getName()  # Example method call
        return PlainTextResponse('hello, %s!')

    @classmethod
    async def getusername(self, request):
        name = self.customer_service.getName()
        print(name)
