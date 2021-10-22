from rest_framework import serializers

from api_garden.models import User
from api_base.utils.user import UserUtils


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        password = validated_data.get("password")
        hashed_password = UserUtils.hash_password(password)
        validated_data["password"] = hashed_password

        return self.create(validated_data)
