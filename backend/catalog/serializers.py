from rest_framework import serializers
from catalog.models import Product
from content.serializers import CulturalMotifSerializer

class ProductSerializer(serializers.ModelSerializer):
    motifs = CulturalMotifSerializer(many=True, read_only=True)
    
    class Meta:
        model = Product
        fields = ['name', 'price', 'motifs']
        