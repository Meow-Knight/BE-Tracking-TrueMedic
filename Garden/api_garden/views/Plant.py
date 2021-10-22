from api_base.views import BaseViewSet
from api_garden.models import Plant
from api_garden.serializers import PlantSerializer


class PlantViewSet(BaseViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
