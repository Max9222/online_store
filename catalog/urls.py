from django.urls import path
from django.utils.translation.trans_real import catalog

from catalog.views import index, index_1

urlpatterns = [
    path('', index),
    path('contacts/', index_1)
]
