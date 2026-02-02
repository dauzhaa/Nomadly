from django.db import models
from core.models import TimeStampedModel
from content.models import CulturalMotif

class Product(TimeStampedModel):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField(default=0)
    image = models.ImageField(upload_to='generated/', blank=True, null=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - ${self.price}"
    
    motifs = models.ManyToManyField(CulturalMotif, related_name='products')