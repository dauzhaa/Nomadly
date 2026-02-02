from django.db import models
from core.models import TimeStampedModel

# Create your models here.
class CulturalMotif(TimeStampedModel):
    name = models.CharField(max_length=50)
    story = models.TextField()
    region = models.CharField(max_length=10)
    image = models.ImageField(upload_to='generated/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.name} - {self.region}"