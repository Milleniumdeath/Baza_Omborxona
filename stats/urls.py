from django.urls import path

from .views import *

urlpatterns = [
    path('sales/', SalesView.as_view(), name='sales')
]