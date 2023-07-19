from starlette.endpoints import HTTPEndpoint
from starlette.responses import JSONResponse, Response
from starlette.requests import Request


class BaseController(HTTPEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
