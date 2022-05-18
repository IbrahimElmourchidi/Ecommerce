from django.shortcuts import render, redirect
from .models import *
from .forms import SignupForm
from django.contrib.auth import authenticate, login
import json
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string


# Create your views here.


def home(request):
    banners = Banner.objects.all()
    data = Product.objects.all().order_by('-id')[:4]
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
    context = {
        "data": data,
        "product_type": "all",

    }
    return render(reqeust, 'product_list.html', context)


def category_product_list(request, cat_id):
    category = Category.objects.get(id=cat_id)
    data = Product.objects.filter(category=category).order_by('-id')
    context = {
        "data": data,
        "product_type": category.title,
    }
    return render(request, 'product_list.html', context)


def brand_product_list(request, brand_id):
    brand = Brand.objects.get(id=brand_id)
    data = Product.objects.filter(brand=brand).order_by('-id')
    context = {
        "data": data,
        "product_type": brand.title,
    }
    return render(request, 'product_list.html', context)


def product_detail(reqeust, slug, id):
    product = Product.objects.get(id=id)
    context = {
        "data": product,
    }
    return render(reqeust, 'product_detail.html', context)


def signup(request):
    form = SignupForm(request.POST)
    if form.is_valid():
        user = form.save()
        # username = form.cleaned_data.get('username')
        # password = form.cleaned_data.get('password')
        # user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    context = {
        "form": form
    }
    return render(request, 'registration/signup.html', context)


def add_to_cart(request):
    # del request.session['cartdata']
    cart_p = {}
    cart_p[str(request.GET['id'])] = {
        'image': request.GET['image'],
        'title': request.GET['title'],
        'qty': request.GET['qty'],
        'price': request.GET['price'],
    }
    if 'cartdata' in request.session:
        if str(request.GET['id']) in request.session['cartdata']:
            cart_data = request.session['cartdata']
            cart_data[str(request.GET['id'])]['qty'] = int(
                cart_p[str(request.GET['id'])]['qty'])
            cart_data.update(cart_data)
            request.session['cartdata'] = cart_data
        else:
            cart_data = request.session['cartdata']
            cart_data.update(cart_p)
            request.session['cartdata'] = cart_data
    else:
        request.session['cartdata'] = cart_p
    return JsonResponse({'data': request.session['cartdata'], 'totalitems': len(request.session['cartdata'])})

# Cart List Page


def cart_list(request):
    total_amt = 0
    if 'cartdata' in request.session:
        for p_id, item in request.session['cartdata'].items():
            total_amt += int(item['qty'])*float(item['price'])
        return render(request, 'cart.html', {'cart_data': request.session['cartdata'], 'totalitems': len(request.session['cartdata']), 'total_amt': total_amt})
    else:
        return render(request, 'cart.html', {'cart_data': '', 'totalitems': 0, 'total_amt': total_amt})


# Delete Cart Item
def delete_cart_item(request):
    p_id = str(request.GET['id'])
    if 'cartdata' in request.session:
        if p_id in request.session['cartdata']:
            cart_data = request.session['cartdata']
            del request.session['cartdata'][p_id]
            request.session['cartdata'] = cart_data
    total_amt = 0
    for p_id, item in request.session['cartdata'].items():
        total_amt += int(item['qty'])*float(item['price'])
    t = render_to_string('ajax/cart-list.html', {'cart_data': request.session['cartdata'], 'totalitems': len(
        request.session['cartdata']), 'total_amt': total_amt})
    return JsonResponse({'data': t, 'totalitems': len(request.session['cartdata'])})

# update Cart Item


def update_cart_item(request):
    p_id = str(request.GET['id'])
    p_qty = request.GET['qty']
    if 'cartdata' in request.session:
        if p_id in request.session['cartdata']:
            cart_data = request.session['cartdata']
            cart_data[str(request.GET['id'])]['qty'] = p_qty
            request.session['cartdata'] = cart_data
    total_amt = 0
    for p_id, item in request.session['cartdata'].items():
        total_amt += int(item['qty'])*float(item['price'])
    t = render_to_string('ajax/cart-list.html', {'cart_data': request.session['cartdata'], 'totalitems': len(
        request.session['cartdata']), 'total_amt': total_amt})
    return JsonResponse({'data': t, 'totalitems': len(request.session['cartdata'])})
