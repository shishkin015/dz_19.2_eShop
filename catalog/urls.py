from django.urls import path, re_path
from catalog.views import index, contact

urlpatterns = [
    re_path(r'^contact', contact),
    path('', index),
]
