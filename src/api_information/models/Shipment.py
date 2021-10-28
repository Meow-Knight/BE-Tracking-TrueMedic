from django.db import models

from api_base.models import TimeStampedModel
from api_information.models import Medicine, Producer


class Shipment(TimeStampedModel):
    quantity = models.PositiveIntegerField()
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    produced_by = models.ForeignKey(Producer, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'shipment'
