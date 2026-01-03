from django.contrib import admin
from .models import Cart

# Register your models here.
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['session', 'product', 'quantity', 'created_at']
    list_filter = ['product', 'quantity', 'created_at']
    search_fields = ['product']
    date_hierarchy = 'created_at'
    ordering = ['quantity', 'created_at']