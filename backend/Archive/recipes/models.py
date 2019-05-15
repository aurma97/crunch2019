from django.db import models
from django.contrib.auth.models import User
from ..products.models import Products

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Recipes(models.Model):
    ingredient = models.CharField(max_length=100)
    indice_nut = models.CharField(max_length=100)
    calories = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    nb_people = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    comments = models.TextField(max_length=1000)
    category = models.ForeignKey(Category, default=None, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add= True)
    
    def __str__(self):
        return self.ingredient

class Preparation(models.Model):
    recipe = models.ForeignKey(Recipes, default=None, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, default=None, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add= True)
    created_for = models.DateTimeField()
    
    def __str__(self):
        return self.recipe