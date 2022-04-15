import json
import os.path
from json import load

from django.shortcuts import render

from mainapp.models import Product, ProductCategories

base_dir = os.path.dirname(__file__)
# Create your views here.

def jsonloader(file_name):
    with open(os.path.join(base_dir, file_name), 'r', encoding='utf-8') as json_obj:
        return json.load(json_obj)

def index(request):
    context = {'title': 'geekshop'}
    return render(request, 'mainapp/index.html', context)




def products(request):
    context = {'title': "geekShop - Каталог",
               'categories': ProductCategories.objects.all(),
               'products': Product.objects.all()}

    return render(request, 'mainapp/products.html', context)
