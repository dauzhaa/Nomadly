from django.contrib import admin
from .models import Order, OrderItems

# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItems
    raw_id_fields = ('product',)
    extra = 0
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['session', 'full_name', 'address', 'total_amount', 'status', 'created_at']
    list_filter = ['full_name', 'address', 'total_amount', 'status']
    search_fields = ['full_name', 'address']
    date_hierarchy = 'created_at'
    ordering = ['total_amount', 'status']
    
    inlines = [OrderItemInline]
    
@admin.register(OrderItems)
class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price']