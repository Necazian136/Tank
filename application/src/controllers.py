from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.utils.decorators import method_decorator
from application.src.manager import TankManager


@method_decorator(csrf_exempt, name='dispatch')
class TankController(View):

    def __init__(self, **kwargs):
        self.tank_manager = TankManager()
        super().__init__(**kwargs)

    def get(self, request, name):
        self.tank_manager.action(name)
        return HttpResponse('')
