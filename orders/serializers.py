from rest_framework import serializers
from .models import Order, OrderItems

class OrderItemsSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')

    class Meta:
        model = OrderItems
        fields = ['id', 'product', 'product_name', 'quantity', 'price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemsSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = ['id', 'full_name', 'address', 'total_amount', 'status', 'items']