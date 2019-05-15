from django.contrib import admin
from .models import Products, ProductCategory, ProductsByProducer, Producers
# Register your models here.
admin.site.register(Products)
admin.site.register(ProductCategory)
admin.site.register(ProductsByProducer)
admin.site.register(Producers)