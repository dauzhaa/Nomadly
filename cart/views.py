from django.shortcuts import render
from rest_framework import viewsets
from cart.serializers import CartSerializer
from cart.models import Cart

class CartViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer   