from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from product.models import Categories
from product.serializer import CategorySerializer


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
def update_cate(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save
        return Response(serializer.data)

@api_view(['POST'])
def add_cate(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
