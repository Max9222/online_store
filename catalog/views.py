from django.shortcuts import render

from catalog.models import Product


def index(request):
    if request.method == 'POST':
        print(**request.POST)

    context = {
        'title': 'Главная'
    }
    return render(request, 'catalog/index.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')

    context = {
        'title': 'Контакт'
    }
    return render(request, 'catalog/contact.html', context)


def product(request):
    product_list = Product.objects.all()
    print(product_list)
    context = {
        'object_list': product_list,
        'title': 'Продукт'
    }
    return render(request, 'catalog/product.html', context)
