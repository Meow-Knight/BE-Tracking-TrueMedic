from rest_framework import serializers

from api_information.models import Medicine


class MedicineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Medicine
        fields = '__all__'
