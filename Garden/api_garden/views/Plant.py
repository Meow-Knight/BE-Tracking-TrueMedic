from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q

from api_base.views import BaseViewSet
from api_garden.models import Plant
from api_garden.serializers import PlantSerializer


class PlantViewSet(BaseViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

    @action(methods=["get"], detail=False)
    def search(self, request, *args, **kwargs):
        request_name = request.query_params.get("q")
        query_set = Plant.objects.filter(name__contains=request_name)
        serializer = self.get_serializer(query_set, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
