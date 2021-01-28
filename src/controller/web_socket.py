import websocket


class WebSocketController:
    def __init__(self, mediator):
        self.mediator = mediator
        websocket.enableTrace(True)

        def on_message(ws, message):
            print(message)
            self.mediator.call(message)

        def on_error(ws, error):
            print(error)

        def on_close(ws):
            print("closed")

        def on_open(ws):
            ws.send('transmitter')

        ws = websocket.WebSocketApp(
            "wss://websocket-necazian.herokuapp.com/",
            on_message=on_message,
            on_error=on_error,
            on_close=on_close,
            on_open=on_open
        )
        ws.run_forever()
