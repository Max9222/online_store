
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import contact, product, IndexListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('contact/', contact, name='contact'),
    path('product/', product, name='product')
]
