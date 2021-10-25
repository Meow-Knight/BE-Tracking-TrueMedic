from rest_framework import serializers

from django.contrib.auth.hashers import make_password

from api_garden.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        password = validated_data.get("password")
        hashed_password = make_password(password)
        validated_data["password"] = hashed_password

        return super().create(validated_data)
