from django.urls import path
from django.views.generic import TemplateView
from .views import ListProducts, ProductUdView, ProductReadView, ProductCreateView

urlpatterns = [ 

    #Show whole Products
    # url = http://localhost:8000/api/manage/Products/
    path('', ListProducts.as_view()),

    # url = http://localhost:8000/api/manage/Products/create
    path('create', ProductCreateView.as_view()),

    #Update or Delete specific Product
    # url = http://localhost:8000/api/manage/Products/update-or-delete/1
    path('update-or-delete/<pk>', ProductUdView.as_view()),

    #Show a specific Product
    # url = http://localhost:8000/api/manage/Products/show/1
    path('show/<pk>', ProductReadView.as_view(), name="Product-rud"),
]