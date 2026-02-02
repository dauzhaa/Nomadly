from django.db import models
from django.contrib.sessions.models import Session
from core.models import TimeStampedModel
from django.conf import settings

from catalog.models import Product


class Cart(TimeStampedModel):
    session_key = models.CharField(max_length=40, db_index=True)
    product= models.ForeignKey(Product, on_delete=models.CASCADE, related_name='in_carts')
    quantity = models.IntegerField(default=1)

    class Meta:
        unique_together = ['session_key', 'product']
        ordering = ['-created_at']
        
    def __str__(self):
        return f'Cart({self.session_key[:8]}...): {self.product.name}'    

    @property
    def subtotal(self):
        return self.quantity * self.product.price
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart', blank=True, null=True)
    
    
    