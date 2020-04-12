from rest_framework import serializers
from .models import Item, Category

class ItemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields= '__all__'
