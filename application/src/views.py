from django.http import StreamingHttpResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import View

import time


class StreamView(View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        from Tank.wsgi import camera
        self.camera = camera

    def gen(self):
        while True:
            time.sleep(0.2)
            buf = self.camera.buf

            if buf is not None:
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + bytearray(buf) + b'\r\n\r\n')
            yield None

    def get(self, request):
        try:
            if self.camera.is_active or self.camera.restart():
                return StreamingHttpResponse(self.gen(), status=206,
                                             content_type="multipart/x-mixed-replace;boundary=frame")
        except Exception as e:
            pass
        return HttpResponse('')


class Main(View):
    def get(self, request):
        return render(request, 'main/main.html')
