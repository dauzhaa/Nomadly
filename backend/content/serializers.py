from rest_framework import serializers
from content.models import CulturalMotif

class CulturalMotifSerializer(serializers.ModelSerializer):
    class Meta:
        model = CulturalMotif
        fields = ['id', 'name', 'story', 'image']
        