import time
import cv2
import threading
# import RPi.GPIO as GPIO


class Camera:
    def __init__(self):
        #GPIO.setmode(GPIO.BCM)
        #GPIO.setup(7, GPIO.OUT)
        self.cap = cv2.VideoCapture(0)
        self.delay = 15
        self.frame = None
        self.buf = None
        self.file_path = 'application/static/images/camera_view.png'
        self.is_active = False
        self.__in_stream = False
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
                        r, self.buf = cv2.imencode(".jpg", self.frame)
                        cv2.imwrite(self.file_path, self.frame)
                    else:
                        self.is_active = False
                        break
            except Exception:
                self.is_active = False
        self.__in_stream = False

    def __del__(self):
        pass
        # GPIO.cleanup()
