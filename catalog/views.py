from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView

from catalog.models import Product, Blog


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

#####

class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'preview',)
    success_url = reverse_lazy('catalog:index')

class BlogListView(ListView):
    model = Blog

class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object



