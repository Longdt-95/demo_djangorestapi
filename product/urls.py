from django.contrib import admin
from django.urls import path

from .views import add_cate, get_all, update_cate, delete_cate, add_product, get_all_product

urlpatterns = [
    path('api/new', add_cate),
    path('api/all', get_all),
    path('api/update/<str:pk>/', update_cate),
    path('api/delete/<str:pk>/', delete_cate),
    path('api/product/new', add_product),
    path('api/product/all', get_all_product)
]
