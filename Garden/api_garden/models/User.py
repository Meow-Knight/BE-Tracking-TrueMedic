from django.db import models
from api_base.models import TimeStampedModel


class User(TimeStampedModel):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, null=True, blank=True)
    avatar = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = "users"
