from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    return render(request, 'index.html')


def category_list(reqeust):
    data = Category.objects.all().order_by('-id')
    context = {
        "categories": data
    }

    return render(reqeust, 'category_list.html', context)


def brand_list(reqeust):
    data = Brand.objects.all().order_by('-id')
    context = {
        "brands": data
    }

    return render(reqeust, 'brand_list.html', context)
