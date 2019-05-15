from django.db.models import Q
from django.http import HttpResponse
from django.db import connection
from rest_framework import generics, mixins
from rest_framework.response import Response
from .models import Products
from .serializer import ProductsSerializer, ListProductsSerializer


#################################
# Create Update And Delete Only #
################################

#Add an Product (Can also see an Product but list is not detailed)
class ProductCreateView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


#Update and Delete and Equipement
class ProductUdView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = ProductsSerializer
    pass

    def get_queryset(self):
        post = Products.objects.all()
        return post


##################################################
# List Only  #
##################################################

class ListProducts(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = ListProductsSerializer
    queryset = Products.objects.all()

#Specific Equipement
class ProductReadView(generics.RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = ListProductsSerializer
    queryset = Products.objects.all()