from rest_framework import serializers
from .models import Item  # Adjust the import according to your model name

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'description']  # Include all the fields you want to expose
