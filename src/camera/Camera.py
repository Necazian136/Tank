import base64
import time
import cv2
import threading


class Camera:
    def __init__(self, mediator):
        self.frame = None
        self.buf = None
        self.file_path = 'image/camera_view.jpg'
        self.is_active = False
        self.__in_stream = False
        self.mediator = mediator
        self.mediator.register('get_image_data', self.get_image_data)

        self.restart()

    def restart(self):
        if not (self.is_active or self.__in_stream):
            self.cap = cv2.VideoCapture(0)
            t = threading.Thread(target=self.stream, args=())
            t.start()
            if self.is_active:
                return True
        return False

    def stream(self):
        self.__in_stream = True
        while True:
            try:
                time.sleep(0.1)
                if self.cap is not None:
                    ret, self.frame = self.cap.read()
                    if self.frame is not None:
                        if not self.is_active:
                            self.is_active = True
                        self.frame = cv2.resize(self.frame, (80, 60))
                        r, self.buf = cv2.imencode(".jpg", self.frame)
                        self.mediator.call('on_image_save')
                    else:
                        self.is_active = False
                        break
            except Exception:
                self.is_active = False
        self.__in_stream = False

    def get_image_data(self):
        return base64.b64encode(self.buf)
