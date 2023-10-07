from django.shortcuts import render
from django.views.generic import ListView, DetailView

from catalog.models import Product


class IndexListView(ListView):
    model = Product
    template_name = 'catalog/index.html'



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


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product.html'


class ProductDetailView(DetailView):
    model = Product
