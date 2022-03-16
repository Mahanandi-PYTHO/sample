from django.db import models
from django.db.models.expressions import OrderBy


# Create your models here.

import common.models as common_model



class FlowQueries(common_model.BaseModel):

    queries = models.TextField(max_length=255)
    response = models.BooleanField(default=False)

    class Meta:
        db_table = "flow_queries"
        ordering = ['-created_on']



class ChatFlowLog(common_model.BaseModel):

    profile_name = models.CharField(max_length=255)
    contact_number = models.PositiveIntegerField()
    messaged_by = models.CharField(max_length=20, choices=(("BOT", "BOT"),("CANDIDATE", "CANDIDATE")))
    message_status = models.CharField(max_length=30, default='sent')
     
    class Meta:
        db_table = "chat_flow_log"
        ordering = ['-updated_on']
