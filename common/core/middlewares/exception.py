from django.conf import settings
from django.http import JsonResponse

class ExceptionMiddleware(object):

    def __init__(self, get_response=None):
        self.get_response = get_response
        super(ExceptionMiddleware, self).__init__()
    
    def __call__(self, request):
        return self.get_response(request)
    
    def process_exception(self, request, exception):
        response = dict()
        if hasattr(exception, 'message'):
            message = str(exception.message)
        elif settings.DEBUG:
            message = str(exception).replace("'", "").title()
        else:
            message = "Something Went Wrong"
        response["message"] = message
        response["info"] = dict(exception.payload or ()) if hasattr(exception, 'payload') else {"hint": "Service Broke Down"}
        response["info"]["type"] = "error"
        response["info"]["appCode"] = exception.app_code if hasattr(exception, 'app_code') else str("MDLW500")
        return JsonResponse(response, status=exception.status if hasattr(exception, 'status') else 500)
