
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import contact, IndexListView, ProductListView, ProductDetailView, BlogCreateView, BlogListView, \
    BlogDetailView, BlogUpdateView, toggle_activity

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('contact/', contact, name='contact'),
    path('product/', ProductListView.as_view(), name='product_list'),
    path('view<int:pk>/', ProductDetailView.as_view(), name='product_view'),
    path('create/', BlogCreateView.as_view(), name='create_blog'),
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_view'),
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name='blog_edit'),
    path('activity/<int:pk>/', toggle_activity, name='toggle_activity'),

]
