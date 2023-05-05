from rest_framework import serializers
from .models import *

class DataScrapingSerializer(serializers.ModelSerializer):
     class Meta:
        model= DataScraping
        fields = '__all__'
           
     def create(self, validate_data):
         return DataScraping.objects.create(**validate_data)