from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.utils.translation.trans_real import catalog

from catalog.views import index, contact, product

urlpatterns = [
    path('', index),
    path('contacts/', contact),
    path('products/', product)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
