# myapp/middleware.py
from rest_framework.request import Request
from api.models import Device

class CustomRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        

    def __call__(self, request):
        try:
            device_id=request.headers["Device-Id"]
            any=Device.objects.filter(device_id=device_id)
            if any.exists():
                request.device=any.first()
            else:
                request.device=Device.objects.create(
                device_id=device_id
        )
        except:
            request.device=None
        # You can add any other logic here before passing the request to the next middleware or view.
        response = self.get_response(request)
        # You can add any logic here after processing the view response.
        return response