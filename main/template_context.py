from .models import *


def get_filters(request):
    cats = Product.objects.distinct().values('category__title', 'category__id')
    colors = ProductAttribute.objects.distinct().values(
        'color__color_code', 'color__id')
    brands = Product.objects.distinct().values('brand__title', 'brand__id')
    sizes = ProductAttribute.objects.distinct().values('size__title', 'size__id')
    return {
        "cats": cats,
        "colors": colors,
        "brands": brands,
        "sizes": sizes,
    }
