from django.urls import path
from .views import *

from django.conf import settings
from django.conf.urls.static import static
import json
from django.http import HttpResponse

urlpatterns = [
    path('', home, name="home"),
    path('category-list', category_list, name='category-list'),
    path('brand-list', brand_list, name='brand-list'),
    path('product-list', product_list, name='product-list'),
    path('category-product-list/<int:cat_id>', category_product_list,
         name='category-product-list'),
    path('brand-product-list/<int:brand_id>', brand_product_list,
         name='brand-product-list'),
    path('product/<str:slug>/<int:id>', product_detail,
         name='product-detail'),
    path('accounts/signup', signup,
         name='signup'),
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_list, name='cart'),
    path('delete-from-cart/', delete_cart_item, name='delete-from-cart'),
    path('update-cart/', update_cart_item, name='update-cart'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
