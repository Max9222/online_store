from django.shortcuts import render
from django.views.generic import ListView, DetailView

from catalog.models import Product


class IndexListView(ListView):
    model = Product
    template_name = 'catalog/index.html'


# def index(request):
#     if request.method == 'POST':
#         print(**request.POST)
#
#     context = {
#         'object_list': Product.objects.all(),
#         'title': 'Главная'
#     }
#     return render(request, 'catalog/index.html', context)


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


# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'catalog/product.html'
def product(request):
    product_list = Product.objects.all()

    context = {
        'object_list': product_list,
        'title': 'Продукт'
    }
    return render(request, 'catalog/product.html', context)
