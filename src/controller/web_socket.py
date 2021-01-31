import time

import websocket


class WebSocketController:
    def __init__(self, mediator):
        self.mediator = mediator
        self.ws = None
        websocket.enableTrace(False)

        self.connect()

    def connect(self):
        def on_message(ws, message):
            print(message)
            self.mediator.call(message)

        def on_error(ws, error):
            print(error)

        def on_close(ws):
            time.sleep(10)

        def on_open(ws):
            ws.send('transmitter')

        self.ws = websocket.WebSocketApp(
            "wss://websocket-necazian.herokuapp.com/",
            on_message=on_message,
            on_error=on_error,
            on_close=on_close,
            on_open=on_open
        )
        self.mediator.register('on_image_save', self.send_image)

        self.ws.run_forever()

        self.connect()

    def send_image(self):
        img_base64 = self.mediator.call('get_image_data')
        self.ws.send(img_base64)
