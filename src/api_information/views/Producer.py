from rest_framework import viewsets

from api_information.models import Producer
from api_information.serializers import ProducerSerializer


class ProducerViewSet(viewsets.ModelViewSet):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer
