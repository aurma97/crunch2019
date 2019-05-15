from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ProductCategory(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

class Products(models.Model):
    product_name = models.CharField(max_length=100)
    isUnit = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    calories = models.CharField(max_length=100)
    category = models.ForeignKey(ProductCategory, default=None, on_delete=models.CASCADE)
    caliber = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    created_by = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.product_name

class ProductsByProducer(models.Model):
    products = models.ForeignKey(Products, default=None, on_delete=models.CASCADE)
    producer = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.producer

class Producers(models.Model):
    producer_name = models.CharField(max_length=100)

    def __str__(self):
        return self.producer_name