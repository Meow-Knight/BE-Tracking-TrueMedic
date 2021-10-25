from rest_framework import serializers

from api_information.models import MedicineUnit


class MedicineUnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = MedicineUnit
        fields = '__all__'
