from rest_framework import serializers
from cart.models import Cart
from catalog.serializers import ProductSerializer

class CartSerializer(serializers.ModelSerializer):
    product_details = ProductSerializer(source='product', read_only=True)
    
    class Meta:
        model = Cart
        fields = ['id', 'product', 'product_details', 'quantity', 'subtotal']