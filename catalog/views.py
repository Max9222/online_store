from django.shortcuts import render

from catalog.models import Product


def index(request):
    if request.method == 'POST':
        print(**request.POST)

    return render(request, 'catalog/index.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')

    return render(request, 'catalog/contact.html')


def product(request):
    product_list = Product.objects.all()
    print(product_list)
    context = {
        'object_list': product_list
    }
    return render(request, 'catalog/product.html', context)
