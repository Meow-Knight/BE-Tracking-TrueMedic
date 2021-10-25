from django.db import models

from api_base.models import TimeStampedModel


class Agent(TimeStampedModel):
    business_code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        db_table = 'agent'
