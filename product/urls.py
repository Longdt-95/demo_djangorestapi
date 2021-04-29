from django.contrib import admin
from django.urls import path

from .views import add_cate, get_all

urlpatterns = [
    path('api/new', add_cate),
    path('api/all', get_all),
]