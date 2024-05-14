from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, User
from .serializers import ProductSerielizer
import random

class ProductViewSet(viewsets.ViewSet):
    # handle get request /api/products
    def list(self, request):
        products = Product.objects.all()
        serializer  = ProductSerielizer(products, many=True)
        return Response(serializer.data)
    # handle post request /api/products
    def create(self, request):
        serializer = ProductSerielizer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    # handle post request /api/products/<str:id>
    def retrieve(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer=  ProductSerielizer(product)
        return Response(serializer.data)
    # handle put request /api/products/<str:id>
    def update(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerielizer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
    
    # handle delete  request /api/products/<str:id>
    def destroy(self, request, pk=None):
        product = Product.objects.get(id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        user = random.choice(users)
        return Response({
            'id':user.id
        })