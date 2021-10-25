from django.db import models

from api_base.models import TimeStampedModel
from api_information.models import MedicineUnit


class Medicine(TimeStampedModel):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=200, null=True, blank=True)
    uses = models.TextField(null=True, blank=True)
    unit = models.ForeignKey(MedicineUnit, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'medicine'
