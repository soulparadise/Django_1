import json

from django.core.management import BaseCommand

from authapp.models import User
from mainapp.models import Product, ProductCategories



def load_json(file):
    with open(file, 'r', encoding='utf-8') as json_obj:
        return json.load(json_obj)

class Command(BaseCommand):
    def handle(self, *args, **options):

        User.objects.create_superuser(username='admin', email='admin@admin.ru', password='admin')
        categories = load_json('mainapp/fixtures/categories.json')

        ProductCategories.objects.all().delete()

        for category in categories:
            cat = category.get('fields')
            cat['id'] = category.get('pk')
            new_category = ProductCategories(**cat)
            new_category.save()

        products = load_json('mainapp/fixtures/products.json')

        Product.objects.all().delete()
        for product in products:
            prod = product.get('fields')
            category = prod.get('category')
            _category = ProductCategories.objects.get(id=category)
            prod['category'] =_category
            new_category = Product(**prod)
            new_category.save()
