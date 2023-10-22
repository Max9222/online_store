from django.forms import inlineformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from catalog.forms import ProductForm, PossibilitiesForm, VersionForm
from catalog.models import Product, Blog, Possibilities, Version

from django.urls import reverse


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
    success_url = reverse_lazy('catalog:blog_list')


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content', 'preview',)
    success_url = reverse_lazy('catalog:blog_list')


class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:list')

def toggle_activity(request, pk):
    blog_item = get_object_or_404(Blog, pk=pk)
    if blog_item.is_active:
        blog_item.is_active = False
    else:
        blog_item.is_active = True

    blog_item.save()

    return redirect(reverse('catalog:index'))


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    #success_url = reverse_lazy('catalog:index')

    def get_success_url(self):
        return reverse('catalog:update_product', args=[self.kwargs.get('pk')])
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)

        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)

    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     PossibilitiesFormset = inlineformset_factory(Product, Possibilities, form=PossibilitiesForm, extra=1)
    #     if self.request.method == 'POST':
    #         context_data['formset'] = PossibilitiesFormset(self.request.POST, instance=self.object)
    #     else:
    #         context_data['formset'] = PossibilitiesFormset(instance=self.object)
    #     return context_data
    #
    # def form_valid(self, form):
    #     formset = self.get_context_data()['formset']
    #     self.object = form.save()
    #     if formset.is_valid():
    #         formset.instance = self.object
    #         formset.save()
    #
    #     return super().form_valid(form)



