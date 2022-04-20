import json
import os.path
from json import load

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views.generic import DetailView

from mainapp.models import Product, ProductCategories

base_dir = os.path.dirname(__file__)


# Create your views here.

def jsonloader(file_name):
    with open(os.path.join(base_dir, file_name), 'r', encoding='utf-8') as json_obj:
        return json.load(json_obj)


def index(request):
    context = {'title': 'geekshop'}
    return render(request, 'mainapp/index.html', context)


def products(request, id_category=None, page=1):
    if id_category:
        products_ = Product.objects.filter(id=id_category)
    else:
        products_ = Product.objects.all()

    pagination = Paginator(products_, per_page=2)

    try:
        product_pagination = pagination.page(page)
    except PageNotAnInteger:
        product_pagination = pagination.page(1)
    except EmptyPage:
        product_pagination = pagination.page(pagination.num_pages)



    context = {'title': "geekShop - Каталог",
               'categories': ProductCategories.objects.all(),
               'products': product_pagination
               }

    return render(request, 'mainapp/products.html', context)

class ProductDetail(DetailView):
    model = Product
    template_name = 'mainapp/detail.html'