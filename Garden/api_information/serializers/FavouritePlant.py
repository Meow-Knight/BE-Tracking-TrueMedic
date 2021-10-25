from rest_framework import serializers

from api_garden.models import FavouritePlant


class FavouritePlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavouritePlant
        fields = '__all__'
