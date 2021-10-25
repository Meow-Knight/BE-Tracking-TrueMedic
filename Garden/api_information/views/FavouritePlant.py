from api_base.views import BaseViewSet

from api_garden.models import FavouritePlant
from api_garden.serializers import FavouritePlantSerializer


class FavouritePlantViewSet(BaseViewSet):
    queryset = FavouritePlant.objects.all()
    serializer_class = FavouritePlantSerializer
