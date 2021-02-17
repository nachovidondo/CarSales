from rest_framework import serializers
from apps.autos.models import Category,Importation

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('created_date','modifieda_date','delete_date')
        
class ImportationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Importation
        exclude = ('created_date','modifieda_date','delete_date')
        
        
