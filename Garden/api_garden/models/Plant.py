from django.db import models
from api_base.models import TimeStampedModel


class Plant(TimeStampedModel):
    name = models.CharField(max_length=50, unique=True)
    image = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    region = models.CharField(max_length=50)
    care_tips = models.TextField(null=True, blank=True)
    benefits = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "plants"
