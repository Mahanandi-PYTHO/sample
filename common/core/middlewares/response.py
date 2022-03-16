from django.http import JsonResponse
try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object

import humps

import common.core.routes as all_routes

class HttpResponseFormatter(MiddlewareMixin):
    """
    For formating the http response sent by service
    """
    def process_response(self, request, response):
        if hasattr(response, "data"):
            result = {}
            result["result"] = response.data
            result["info"] = {}
            if isinstance(response.data, list):
                result["info"]["count"] = len(response.data)
            result["info"]["hint"] = self._get_hint(response.status_code)
            result["info"]["type"] = "success" if response.status_code in [200, 201, 204] else "error"
            result["info"]["appCode"] = "HRTC"+str(response.status_code)
            return JsonResponse(humps.camelize(result), status=response.status_code)
        return response
    
    def _get_hint(self, status_code):
        messages = {
            200: "Request Successful",
            201: "Created Successfully",
            204: "Request Successful",
            401: "Unauthorized Request",
            400: "Malformed Request Cannot be Processed",
            404: "Requested Resource Not Found",
            500: "Something Went Wrong",
            503: "Service is Unavailable"
        }
        return messages.get(status_code, "")
