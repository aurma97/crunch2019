from django.db.models import Q
from django.http import HttpResponse
from django.db import connection
from rest_framework import generics, mixins
from rest_framework.response import Response
from .models import Recipes, Category
from .serializer import RecipesSerializer, ListRecipesSerializer, ListCategoriesSerializer


#################################
# Create Update And Delete Only #
################################

#Add an Recipes (Can also see an Recipes but list is not detailed)
class RecipesCreateView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = RecipesSerializer
    queryset = Recipes.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


#Update and Delete and Equipement
class RecipesUdView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = RecipesSerializer
    pass

    def get_queryset(self):
        post = Recipes.objects.all()
        return post


##################################################
# List Only  #
##################################################

class ListRecipes(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = ListRecipesSerializer
    queryset = Recipes.objects.all()

class ListCategories(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = ListCategoriesSerializer
    queryset = Category.objects.all()

#Specific Equipement
class RecipesReadView(generics.RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = ListRecipesSerializer
    queryset = Recipes.objects.all()