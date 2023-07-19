from starlette.endpoints import WebSocketEndpoint


class Websocket_endpoint_class(WebSocketEndpoint):
    # encoding = 'bytes'
    encoding = "text"

    async def on_connect(self, websocket):
        await websocket.accept()

    async def on_receive(self, websocket, data):
        # await websocket.send_bytes(b"Message: " + data)
        await websocket.send_text(f"Message text was: {data}")

    async def on_disconnect(self, websocket, close_code):
        websocket.close()
        # pass  *** not implemented..
