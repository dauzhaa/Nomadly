from django.db import models
from django.contrib.sessions.models import Session

from catalog.models import Product


class Cart(models.Model):
    session_key = models.CharField(max_length=40, db_index=True)
    product= models.ForeignKey(Product, on_delete=models.CASCADE, related_name='in_carts')
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['session_key', 'product']
        ordering = ['-created_at']
        
    def __str__(self):
        return f'Cart({self.session_key[:8]}...): {self.product.name}'    

    @property
    def subtotal(self):
        return self.quantity * self.product.price