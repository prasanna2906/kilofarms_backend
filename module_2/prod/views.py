from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product

@api_view(['GET'])
def Productview(request):
    prod_urls = {
        'List' : '/listprods/' ,
        'Detail View': '/product_details/<str:pk>/'  ,
        'Create': '/createSKU/',
        'Update': '/product_update/<str:pk>/', 
        'Delete': '/product_del/<str:pk>/',
    }

    return Response(prod_urls)

@api_view(['GET'])
def productList(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many = True)
    return Response(serializer.data)
  
@api_view(['GET'])
def productDetail(request,pk):
    products = Product.objects.get(id=pk)
    serializer = ProductSerializer(products, many = False)
    return Response(serializer.data)


@api_view(['POST'])
def productCreate(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def productUpdate(request,pk):
    products = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=products, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT'])
def productUpdate(request,pk):
    products = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=products, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def productDelete(request,pk):
    products = Product.objects.get(id=pk)
    products.delete()

    return Response('product deleted')
