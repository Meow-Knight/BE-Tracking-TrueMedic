from django.db import models

from api_base.models import TimeStampedModel


class Medicine(TimeStampedModel):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=200, null=True, blank=True)
    uses = models.TextField(null=True, blank=True)
    unit = models.CharField(max_length=50)

    class Meta:
        db_table = 'medicine'
