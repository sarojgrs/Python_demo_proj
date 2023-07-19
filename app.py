from typing import Container
from starlette.applications import Starlette
from starlette.exceptions import HTTPException, WebSocketException
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette.websockets import WebSocket
from starlette.routing import Route, Mount, WebSocketRoute
from starlette.templating import Jinja2Templates
from starlette.responses import JSONResponse, PlainTextResponse, Response, RedirectResponse, StreamingResponse
import asyncio
import uvicorn
from starlette.endpoints import HTTPEndpoint
from Controller.WebSocket import Websocket_endpoint_class
from Controller.WebSocketClient import ClientUser
from Controller.User import UserController
# from Controller.Abc import Abc
import Routes.RoutesModules as RouteModules
import middleware as Middleware
from DependencyInjection.withService import Container, main
from Controller.VoiceMessageController import VoiceMessageController
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

templates = Jinja2Templates(directory='templates')


ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.environ.get("TWILIO_PHONE_NUMBER")

# Create a Twilio client
twilio_client = Client(ACCOUNT_SID, AUTH_TOKEN)


async def homepage(request):
    template = "index.html"
    name1 = 'saroj'
    context = {"request": request, "name1": name1}
    return templates.TemplateResponse(template, context)


async def getUserName(request: Request):
    username = request.path_params['username']
    address = request.query_params['address']
    return PlainTextResponse('hello, %s!' % username + 'address, %s!' % address)


async def api(request):
    return JSONResponse({'hello': 'helloworld'})


async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    try:
        while True:
            message = await websocket.receive_text()
            # Process the received message
            # ...
            await websocket.send_text('Message received: ' + message)
            break
    except websocket._raise_on_disconnect:
        print('websocket got an issue')
        # Handle disconnection
        # ...

        # Close the WebSocket connection
    await websocket.close()


async def error(request):
    """
    An example error. Switch the `debug` setting to see either tracebacks or 500 pages.
    """
    raise RuntimeError("Oh no")


async def not_found(request: Request, exc: HTTPException):
    """
    Return an HTTP 404 page.
    """
    template = "404.html"
    context = {"request": request}
    return templates.TemplateResponse(template, context, status_code=404)


async def server_error(request: Request, exc: HTTPException):
    """
    Return an HTTP 500 page.
    """
    template = "500.html"
    context = {"request": request}
    return templates.TemplateResponse(template, context, status_code=500)


# Create an instance of the endpoint class
routes = [
    Route('/', homepage),
    # WebSocketRoute('/ws', websocket_endpoint),
    WebSocketRoute('/ws', Websocket_endpoint_class),
    Route('/client', endpoint=ClientUser),
    Route('/error', error),
    Mount('/static', app=StaticFiles(directory='statics'), name='static'),
    Mount('/users', routes=RouteModules.user_routes),
    Mount('/abc', routes=RouteModules.abc_routes),
    Route('/voice', VoiceMessageController),
    Route('/api', endpoint=api)
]


exception_handlers = {
    404: not_found,
    500: server_error
}


def startup():
    print('Ready to go')


app = Starlette(debug=True, routes=routes,
                exception_handlers=exception_handlers, on_startup=[startup], middleware=Middleware.middlewares)

if __name__ == "__main__":
    container = Container()
    # container.config.api_key.from_env("API_KEY", required=True)
    # container.config.timeout.from_env("TIMEOUT", as_=int, default=5)
    container.wire(modules=[__name__])

    main()  # <-- dependencies are injected automatically

    print("server started")
    uvicorn.run(app, host='0.0.0.0', port=8000)
