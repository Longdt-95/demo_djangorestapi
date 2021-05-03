from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

# from .product.models import Categories
from .serializer import CategorySerializer, ProductSerializer

from .models import Categories, Products


@api_view(['GET'])
def get_all(request):
    categories = Categories.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_cate(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)


@api_view(['PUT'])
def update_cate(request, pk):
    category = Categories.objects.get(id=pk)
    serializer = CategorySerializer(instance=category, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)


@api_view(['DELETE'])
def delete_cate(request, pk):
    category = Categories.objects.get(id=pk)
    category.delete()
    return Response("deleted")


@api_view(['GET'])
def get_all_product(request):
    products = Products.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)


# @api_view(['PUT'])
# def update_cate(request, pk):
#     category = Categories.objects.get(id=pk)
#     serializer = CategorySerializer(instance=category, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#
#
# @api_view(['DELETE'])
# def delete_cate(request, pk):
#     category = Categories.objects.get(id=pk)
#     category.delete()
#     return Response("deleted")
