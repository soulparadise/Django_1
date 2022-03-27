from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, 'mainapp/index.html')

def products(request):
    context = {'title': "Каталог",
               'categories': ['Новинки', 'Одежда', 'Обувь', 'Аксессуары', 'Подарки'],
               'products':[{'name': 'Худи черного цвета с монограммами adidas Originals',
                            'price': 6090,
                            'descriprion': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'},
                           {'name': 'Синяя куртка The North Face',
                            'price': 23725,
                            'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'},
                           {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
                            'price': 3390,
                            'description': 'Материал с плюшевой текстурой. Удобный и мягкий.'},
                           {'name': 'Черный рюкзак Nike Heritage',
                            'price': 2340,
                            'description': 'Плотная ткань. Легкий материал.'},
                           {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
                            'price': 13590,
                            'description': 'Гладкий кожаный верх. Натуральный материал.'},
                           {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
                            'price': 2890,
                            'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.'},
                           ]}

    return render(request, 'mainapp/products.html', context)

def test(request):
    context = {'qqq': '/static/vendor/img/products/Black-Dr-Martens-shoes.png'}

    return render(request, 'mainapp/test.html', context)