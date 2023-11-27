from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import IndexView, contact, ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('catalog/<int:pk>', cache_page(60)(ProductListView.as_view()), name='product'),
    path('catalog/create', cache_page(60)(ProductCreateView.as_view()), name='product_create'),
    path('catalog/update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('catalog/delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('contact/', contact, name='contacts'),
]
