from functools import wraps

import common.core.exceptions as common_exceptions

import tenants.models as tenant_model

def authorize_request(function):
    @wraps(function)
    def wrap(method, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION', None)
        if token and tenant_model.Tenant.objects.filter(secret_key=str(token).replace("Bearer ", ""), is_active=True).exists():
            request.META["tenant"] = tenant_model.Tenant.objects.get(secret_key=str(token).replace("Bearer ", ""), is_active=True)
            return function(method, request, *args, **kwargs)
        raise common_exceptions.OnAuthenticationFailedException(
            message="Unauthorised Request. Please provide valid token",
            code="ERRAUTH001"
        )
    return wrap

def authorize_func_request(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION', request.GET.get('token'))
        if token and tenant_model.Tenant.objects.filter(secret_key=str(token).replace("Bearer ", ""), is_active=True).exists():
            request.META["tenant"] = tenant_model.Tenant.objects.get(secret_key=str(token).replace("Bearer ", ""), is_active=True)
            return function(request, *args, **kwargs)
        raise common_exceptions.OnAuthenticationFailedException(
            message="Unauthorised Request. Please provide valid token",
            code="ERRAUTH002"
        )
    return wrap
