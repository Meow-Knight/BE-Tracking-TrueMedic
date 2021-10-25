from rest_framework import serializers

from api_information.models import Shipment


class ShipmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shipment
        fields = '__all__'
