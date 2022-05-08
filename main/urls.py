from django.urls import path
from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home),
    path('category-list', category_list, name='category-list'),
    path('brand-list', brand_list, name='brand-list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
