from rest_framework import serializers
from .models import *

class DataScrapingSerializer(serializers.ModelSerializer):
     class Meta:
        model= WebDataScraping
        fields = '__all__'
           
     def create(self, validate_data):
         return WebDataScraping.objects.create(**validate_data)