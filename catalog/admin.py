from django.contrib import admin
from .models import Product

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock_quantity', 'created_at']
    list_filter = ['name', 'price', 'stock_quantity']
    search_fields = ['name',]
    date_hierarchy = 'created_at'
    ordering = ['price', 'created_at', 'stock_quantity']
    
    
