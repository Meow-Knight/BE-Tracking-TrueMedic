from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

from api_base.models import TimeStampedModel


class User(AbstractBaseUser, TimeStampedModel):
    email = models.EmailField(unique=True)
    eth_address = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, null=True, blank=True)
    avatar = models.CharField(max_length=200, null=True, blank=True)

    USERNAME_FIELD = 'email'

    class Meta:
        db_table = "users"
