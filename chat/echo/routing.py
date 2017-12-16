from channels.routing import route

channel_routing = [
    route('websocket.receive', 'echo.views.ws_receive'),
]
