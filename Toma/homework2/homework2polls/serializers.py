from django.db.models import fields
from rest_framework import serializers
from .models import Car, Board


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'color', 'brand', 'description', 'made']

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['carrier', 'time', 'destination', 'train', 'status']