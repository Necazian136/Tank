from src.camera.Camera import Camera
from src.controller.web_socket import WebSocketController
from src.controller.xbox import XBoxController
from src.mediator.mediator import Mediator
from src.mover.mover import Mover

mediator = Mediator()
mover = Mover(mediator)
xbox = XBoxController(mediator)
camera = Camera(mediator)

web_socket = WebSocketController(mediator)
