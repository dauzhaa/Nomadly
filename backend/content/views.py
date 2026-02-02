from django.shortcuts import render
from rest_framework import viewsets
from content.serializers import CulturalMotifSerializer
from content.models import CulturalMotif

class ContentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CulturalMotif.objects.all()
    serializer_class = CulturalMotifSerializer