# -*- coding: utf-8 -*-
"""
Common Models

CustomBaseModel - For Handling Custom Model
"""

from django.db import models
from django.utils import timezone
import uuid

class BaseModel(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    created_on = models.DateTimeField(
        default=timezone.now
    )
    updated_on = models.DateTimeField(
        auto_now=True
    )
    # archived_on = models.DateTimeField(null=True)
    
    class Meta:
        abstract = True
