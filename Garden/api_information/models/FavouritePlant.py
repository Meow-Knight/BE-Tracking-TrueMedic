from django.db import models

from api_base.models import TimeStampedModel
from api_garden.models import User, Plant


class FavouritePlant(TimeStampedModel):
    user = models.ForeignKey(User, related_name='favourite_plants', on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, related_name='favourite_plants', on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    image = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = "favourite_plants"
