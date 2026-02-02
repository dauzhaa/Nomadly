from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class user(AbstractUser):
    phone_number = models.CharField(max_length=10)
    avatar = models.ImageField(upload_to='generated/', blank=True, null=True)
    bio = models.TextField()
    