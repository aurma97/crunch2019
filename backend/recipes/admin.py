from django.contrib import admin
from .models import Recipes, Category, Preparation
# Register your models here.
admin.site.register(Recipes)
admin.site.register(Category)
admin.site.register(Preparation)