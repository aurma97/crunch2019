from rest_framework import serializers
from .models import Recipes, Category

class RecipesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipes
        fields = ('__all__')
        read_only_fields = ['id']

class ListRecipesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipes
        fields = ('__all__')
        read_only_fields = ['id']
        depth = 1

class ListCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')
        read_only_fields = ['id']
