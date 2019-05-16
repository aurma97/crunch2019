from django.urls import path
from django.views.generic import TemplateView
from .views import ListRecipes, RecipesUdView, RecipesReadView, RecipesCreateView, ListCategories

urlpatterns = [ 
    #Show whole Recipes
    # url = http://localhost:8000/api/manage/Recipes/
    path('', ListRecipes.as_view()),

    path('categories', ListCategories.as_view()),

    # url = http://localhost:8000/api/manage/Recipes/create
    path('create', RecipesCreateView.as_view()),

    #Update or Delete specific Recipes
    # url = http://localhost:8000/api/manage/Recipes/update-or-delete/1
    path('update-or-delete/<pk>', RecipesUdView.as_view()),

    #Show a specific Recipes
    # url = http://localhost:8000/api/manage/Recipes/show/1
    path('show/<pk>', RecipesReadView.as_view(), name="Recipes-rud"),
]