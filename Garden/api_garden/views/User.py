from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q

from api_base.views import BaseViewSet

from api_garden.models import User
from api_garden.serializers import UserSerializer


class UserViewSet(BaseViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # @action(methods=["post"], detail=False)
    # def register(self, request, *args, **kwargs):
    #     register_user_data = request.data
    #
    #     request_name = request.query_params.get("q")
    #
    #     return Response("data", status=status.HTTP_200_OK)
