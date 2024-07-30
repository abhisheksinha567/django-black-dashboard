# home/urls.py
from django.urls import path
from .views import search, add_item, delete_item

urlpatterns = [
    path('search/', search, name='search'),
    path('api/add_item/', add_item, name='add_item'),
    path('api/delete_item/<int:pk>/', delete_item, name='delete_item'),
]
