from django.contrib import admin
from .models import CulturalMotif

@admin.register(CulturalMotif)
class CulturalMotifAdmin(admin.ModelAdmin):
    list_display = ['name', 'region']