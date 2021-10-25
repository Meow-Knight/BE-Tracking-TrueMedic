from rest_framework import viewsets

from api_information.models import MedicineUnit
from api_information.serializers import MedicineUnitSerializer


class MedicineUnitViewSet(viewsets.ModelViewSet):
    queryset = MedicineUnit.objects.all()
    serializer_class = MedicineUnitSerializer
