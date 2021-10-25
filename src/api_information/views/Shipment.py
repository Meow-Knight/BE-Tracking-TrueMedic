from rest_framework import viewsets

from api_information.models import Shipment
from api_information.serializers import ShipmentSerializer


class ShipmentViewSet(viewsets.ModelViewSet):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
