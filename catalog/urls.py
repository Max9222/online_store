
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import contact, IndexListView, ProductListView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('contact/', contact, name='contact'),
    path('product/', ProductListView.as_view(), name='product_list'),
    path('<int:pk/', ProductDetailView.as_view(), name='product_view'),

]
