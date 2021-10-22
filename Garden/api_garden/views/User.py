from api_base.views import BaseViewSet

from api_garden.models import User
from api_garden.serializers import UserSerializer


class UserViewSet(BaseViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
