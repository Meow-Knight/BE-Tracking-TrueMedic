from django.db import models

from api_base.models import TimeStampedModel
from api_information.models import Medicine


class Shipment(TimeStampedModel):
    quantity = models.PositiveIntegerField()
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    image = models.CharField(max_length=200, null=True, blank=True)
    uses = models.TextField(null=True, blank=True)
    unit = models.ForeignKey(Medicine, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'shipment'
