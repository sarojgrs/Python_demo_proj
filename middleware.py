from starlette.middleware import Middleware
from starlette.middleware.trustedhost import TrustedHostMiddleware
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware
from starlette.types import ASGIApp, Message, Scope, Receive, Send
from starlette.requests import Request
from starlette.responses import Response, RedirectResponse
from starlette.authentication import (
    AuthCredentials, AuthenticationBackend, AuthenticationError, SimpleUser
)
from starlette.middleware.authentication import AuthenticationMiddleware


# BaseHTTPMiddleware  it has some limitation..


class CustomHeaderMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, header_value='Example'):
        super().__init__(app)
        self.header_value = header_value

    async def dispatch(self, request, call_next):
        response = await call_next(request)
        response.headers['Custom'] = self.header_value
        return response


class AuthenticationMiddleware1(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        if not self.is_authenticated(request):
            # Redirect the user to the login page
            return RedirectResponse(url="/abc")
        else:
            # User is authenticated, proceed with the request
            response = await call_next(request)
            return response

    def is_authenticated(self, request):
        # Implement your authentication logic here
        # Return True if the user is authenticated, False otherwise
        # You can access request.session, request.cookies, request.headers, etc.
        return True  # Replace with your authentication check


class CustomMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Before "receive" stage
        # Perform preprocessing or modifications on the request
        modified_request = await self.modify_request(request)

        # Call the next middleware or the main application
        response = await call_next(modified_request)

        # After "send" stage
        # Perform post-processing or modifications on the response
        modified_response = self.modify_response(response)

        return modified_response

    async def modify_request(self, request: Request) -> Request:
        # Modify the incoming request, if needed
        # Example: Add custom request headers, modify path parameters, etc.
        return request

    def modify_response(self, response: Response) -> Response:
        # Modify the outgoing response, if needed
        # Example: Add custom response headers, modify response body, etc.
        return response


# pure asgi middleware


class ASGIMiddleware:
    def __init__(self, app: any):
        self.app = app

    async def __call__(self, scope, receive, send):
        await self.app(scope, receive, send)


class LoggedRequestBodySizeMiddleware:
    def __init__(self, app: ASGIApp):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        body_size = 0

        async def receive_logging_request_body_size():
            nonlocal body_size

            message = await receive()
            assert message["type"] == "http.request"

            body_size += len(message.get("body", b""))

            if not message.get("more_body", False):
                print(f"Size of request body was: {body_size} bytes")

            return message

        await self.app(scope, receive_logging_request_body_size, send)


middlewares = [
    # Middleware(AuthenticationMiddleware),
    Middleware(AuthenticationMiddleware1),
    # Middleware(CORSMiddleware, allow_origins=['*']),
    # Middleware(CustomHeaderMiddleware, header_value='Customized'),
    # Middleware(ASGIMiddleware),
    # Middleware(LoggedRequestBodySizeMiddleware),

    # Middleware(HTTPSRedirectMiddleware)
]
