from django.db import models
from django.contrib.auth.models import User
from ..products.models import Products

# Create your models here.

class Commands(models.Model):
    description = models.TextField(max_length=1000)
    product = models.ForeignKey(Products, default=None, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add= True)
    
    def __str__(self):
        return self.description