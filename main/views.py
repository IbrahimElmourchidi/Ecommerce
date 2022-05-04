from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html')


def category_list(reqeust):
    return render(reqeust, 'category_list.html')
