
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import contact, IndexListView, ProductListView, ProductDetailView, BlogCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('contact/', contact, name='contact'),
    path('product/', ProductListView.as_view(), name='product_list'),
    path('view<int:pk>/', ProductDetailView.as_view(), name='product_view'),
    path('create/', BlogCreateView.as_view(), name='create_blog'),
    #path('edit/<int:pk>/', ProductUpdateView.as_view(), name='product_edit')

]
