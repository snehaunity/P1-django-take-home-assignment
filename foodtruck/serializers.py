from rest_framework import serializers
from .models import Foodtruck

class FoodtruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foodtruck
        fields = ['name', 'latitude', 'longitude', 'address']
