from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    banners = Banner.objects.all()
    data = Product.objects.all().order_by('-id')
    print(len(data))
    context = {
        "data": data,
        "banners": banners
    }
    return render(request, 'index.html', context)


def category_list(reqeust):
    data = Category.objects.all().order_by('-id')
    context = {
        "categories": data
    }

    return render(reqeust, 'category_list.html', context)


def brand_list(reqeust):
    data = Brand.objects.all()
    context = {
        "brands": data
    }

    return render(reqeust, 'brand_list.html', context)


def product_list(reqeust):
    data = Product.objects.all().order_by('-id')
    cats = Product.objects.distinct().values('category__title', 'category__id')
    colors = Product.objects.distinct().values('color__color_code', 'color__id')
    brands = Product.objects.distinct().values('brand__title', 'brand__id')
    sizes = Product.objects.distinct().values('size__title', 'size__id')
    context = {
        "data": data,
        "cats": cats,
        "colors": colors,
        "brands": brands,
        "sizes": sizes,
        "product_type": "all",

    }
    return render(reqeust, 'product_list.html', context)


def category_product_list(request, cat_id):
    category = Category.objects.get(id=cat_id)
    data = Product.objects.filter(category=category).order_by('-id')
    colors = Product.objects.distinct().values('color__color_code', 'color__id')
    brands = Product.objects.distinct().values('brand__title', 'brand__id')
    sizes = Product.objects.distinct().values('size__title', 'size__id')
    context = {
        "data": data,
        "colors": colors,
        "brands": brands,
        "sizes": sizes,
        "product_type": category.title,
    }
    return render(request, 'product_list.html', context)


def brand_product_list(request, brand_id):
    brand = Brand.objects.get(id=brand_id)
    data = Product.objects.filter(brand=brand).order_by('-id')
    cats = Product.objects.distinct().values('category__title', 'category__id')
    colors = Product.objects.distinct().values('color__color_code', 'color__id')
    sizes = Product.objects.distinct().values('size__title', 'size__id')
    context = {
        "data": data,
        "cats": cats,
        "colors": colors,
        "product_type": brand.title,
        "sizes": sizes,
    }
    return render(request, 'product_list.html', context)


def product_detail(reqeust, slug, id):
    product = Product.objects.get(id=id)
    context = {
        "data": product,
    }
    return render(reqeust, 'product_detail.html', context)
