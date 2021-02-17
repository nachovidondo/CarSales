from rest_framework import serializers
from apps.autos.models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        exclude = ('created_date','modified_date','delete_date','estado')
        