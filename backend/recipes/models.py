from django.db import models
from django.contrib.auth.models import User
from ..products.models import Products

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Recipes(models.Model):
    name = models.CharField(default=None, max_length=100)
    price = models.CharField(max_length=100)
    ingredient = models.TextField(default=None, max_length=5000)
    duration = models.CharField(default=None, max_length=100)
    category = models.ForeignKey(Category, default=None, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add= True)
    image_one = models.ImageField(null=True, blank=True)
    image_two = models.ImageField(null=True, blank=True)
    image_three = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.name

class Preparation(models.Model):
    recipe = models.ForeignKey(Recipes, default=None, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, default=None, on_delete=models.CASCADE)
    indice_nut = models.CharField(default=None, max_length=100)
    calories = models.CharField(default=None, max_length=100)
    nb_people = models.CharField(default='1', max_length=100)
    created_by = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add= True)
    created_for = models.DateTimeField()