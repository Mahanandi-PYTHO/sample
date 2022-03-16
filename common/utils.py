import secrets
import datetime
import requests
import operator
import os
import mimetypes

from functools import reduce

from subprocess import  Popen

from uuid import UUID

from django.contrib.auth.validators import ASCIIUsernameValidator
from django.core.validators import EmailValidator, RegexValidator
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.db.models import Q

TenantNameRegex = RegexValidator(
    regex=r'^[\w .-]+$', 
    message="Tenant Name Can Only Contain 'alphabets', 'numbers', '-' and '.'"
)

def make_safe_filename(string):
    def safe_char(c):
        if c.isalnum():
            return c
        else:
            return "_"
    string = string.strip().lower()
    return "".join(safe_char(c) for c in string).rstrip("_")

def validate_username(value):
    """
    Validate the name provided
    """
    validator = ASCIIUsernameValidator()
    try:
        validator(value)
        return True
    except:
        return False

def validate_int(value):
    try:
        int(value)
        return True
    except:
        return False

def validate_float(value):
    try:
        float(value)
        return True
    except:
        return False

def validate_tenant_name(value):
    """
    Validate Tenant Name. Can Only Contains 'Alphabets', 'Numbers', '-' and '.'
    """
    try:
        TenantNameRegex(value)
        return True
    except:
        return False

def validate_email(value):
    """
    Validate the provided email
    """
    validator = EmailValidator()
    try:
        validator(value)
        return True
    except:
        return False

def validate_contact_number(value):
    """
    Validate Phone Number
    """
    try:
        ContactNumberRegex(value)
        return True
    except:
        return False

def validate_uuid(value, version=4):
    """
    Validate UUID
    """
    try:
        uuid_obj = UUID(str(value), version=version)
        return str(uuid_obj) == str(value)
    except ValueError:
        return False

def generate_secret(size=64):
    """
    Generate Random Digit Using Python's Default Secret Function
    """
    return secrets.token_urlsafe(size)

def get_origin(request):
    return request.META.get("HTTP_ORIGIN", get_host_ip(request))

def get_host_ip(request):
    host = request.META.get("HTTP_HOST", request.META.get('REMOTE_ADDR'))
    if "http://" not in host or "https://" not in host:
        return request.is_secure() and "https://" or "http://"+host
    return host

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def validate_date(provided_date, compare_with=datetime.datetime.today().date(), condition="less"):
    CONDITIONS = ["less", "greater", "equal", "less or equal", "greater or equal"]
    if compare_with is None:
        try:
            datetime.datetime.strptime(str(provided_date)[:10], "%Y-%m-%d")
            return True
        except:
            return False
    if not provided_date or condition.lower() not in CONDITIONS:
        return False
    input_date = datetime.datetime.strptime(str(provided_date)[:10], "%Y-%m-%d")
    compare_date = datetime.datetime.strptime(str(compare_with)[:10], "%Y-%m-%d")

    if condition.lower() == "less" and not input_date < compare_date:
        return False
    elif condition.lower() == "greater" and not input_date > compare_date:
        return False
    elif condition.lower() == "equal" and not input_date == compare_date:
        return False
    elif condition.lower() == "less or equal" and not input_date <= compare_date:
        return False
    elif condition.lower() == "greater or equal" and not input_date >= compare_date:
        return False
    return True

def send_email(subject:str, message:str, recipients:list, template_path:str, context:dict):
    html_message = render_to_string(template_path, context)
    mail_sent = send_mail(
        subject=subject,
        message=message,
        html_message=html_message,
        recipient_list=recipients if os.environ["ENV"].upper() == "PRODUCTION" else settings.DEFAULT_RECEIPENTS,
        from_email=settings.EMAIL_AUTH_USERNAME,
        auth_user=settings.EMAIL_AUTH_USERNAME,
        auth_password=settings.EMAIL_AUTH_PASSWORD,
        fail_silently=True if os.environ["ENV"].upper() == "PRODUCTION" else False
    )
    return mail_sent
