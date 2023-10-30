from django.conf import settings
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.core.cache import cache
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from catalog.forms import ProductForm, PossibilitiesForm, VersionForm
from catalog.models import Product, Blog, Possibilities, Version

from django.urls import reverse


class IndexListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'catalog/index.html'

@login_required
@permission_required('catalog.view_product')
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


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'catalog/product.html'


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    permission_required = 'catalog.view_product'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        if settings.CACHE_ENABLED:
            key = f'possibilities_list{self.object.pk}'
            possibilities_list = cache.get(key)
            if possibilities_list is None:
                possibilities_list = self.object.possibilities_set.all()
                cache.set(key, possibilities_list)
        else:
            possibilities_list = self.object.possibilities_set.all()

        context_data['possibilities'] = possibilities_list
        return context_data

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:index')
    permission_required = 'catalog.delete_product'


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.crate_product'
    success_url = reverse_lazy('catalog:index')

    def test_func(self):
        return self.request.user.is_superuser

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.change_product'
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

#####

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ('title', 'content', 'preview',)
    success_url = reverse_lazy('catalog:blog_list')


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ('title', 'content', 'preview',)
    success_url = reverse_lazy('catalog:blog_list')


class BlogListView(LoginRequiredMixin, ListView):
    model = Blog


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog_list')

@login_required
def toggle_activity(request, pk):
    blog_item = get_object_or_404(Blog, pk=pk)
    if blog_item.is_active:
        blog_item.is_active = False
    else:
        blog_item.is_active = True

    blog_item.save()

    return redirect(reverse('catalog:index'))
