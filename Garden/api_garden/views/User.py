from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from api_base.views import BaseViewSet

from api_garden.models import User
from api_garden.serializers import UserSerializer
from api_garden.services import UserService


class UserViewSet(BaseViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=["post"], detail=False)
    def login(self, request, *args, **kwargs):
        user_data = request.data

        if UserService.is_valid_login_data(user_data):
            user = User.objects.filter(email=user_data.get('email')).first()
            serializer = self.get_serializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"details": "Email/Password is not correct"},
            status=status.HTTP_400_BAD_REQUEST
        )
