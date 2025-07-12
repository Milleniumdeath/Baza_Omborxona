from django.urls import path

from .views import *

urlpatterns = [
    path('sales/', SalesView.as_view(), name='sales'),
    path('import-products/', ImportProductsView.as_view(), name='import-products'),
]