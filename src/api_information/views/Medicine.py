from rest_framework import viewsets

from api_information.models import Medicine
from api_information.serializers import MedicineSerializer


class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
