from django.shortcuts import render
from rest_framework import viewsets
from orders.models import OrderItems, Order
from orders.serializers import OrderSerializer, OrderItemsSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
class OrderItemsViewSet(viewsets.ModelViewSet):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsSerializer