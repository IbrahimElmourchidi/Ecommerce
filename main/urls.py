from django.urls import path
from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home),
    path('category-list', category_list, name='category-list'),
    path('brand-list', brand_list, name='brand-list'),
    path('product-list', product_list, name='product-list'),
    path('category-product-list/<int:cat_id>', category_product_list,
         name='category-product-list'),
    path('brand-product-list/<int:brand_id>', brand_product_list,
         name='brand-product-list'),
    path('product/<str:slug>/<int:id>', product_detail,
         name='product-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
