from django.db import models
from api_base.models import TimeStampedModel

from phonenumber_field.modelfields import PhoneNumberField


class User(TimeStampedModel):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    phone = PhoneNumberField(null=True, blank=True)
    avatar = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = "users"
