from django.urls import path
from django.utils.translation.trans_real import catalog

from catalog.views import index, contact

urlpatterns = [
    path('', index),
    path('contacts/', contact)
]
