from django.shortcuts import render
from rest_framework import generics, viewsets
from catalog.serializers import ProductSerializer
from catalog.models import Product

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    