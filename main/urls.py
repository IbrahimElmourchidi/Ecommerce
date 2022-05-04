from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('category-list', category_list, name='category-list'),
]
