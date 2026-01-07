from django.db import models
from django.contrib.sessions.models import Session

from catalog.models import Product
    
class Order(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='orders')
    full_name = models.CharField(max_length=255)
    address = models.TextField()    
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, default='paid')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f'Order №{self.id} - {self.full_name} - {self.total_amount}$'
    
class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='order_items')
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f'{self.product.name} x{self.quantity} {self.price}$'
    
    @property
    def subtotal(self):
        return self.quantity * self.price