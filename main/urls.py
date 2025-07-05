from django.urls import path
from .views import *
urlpatterns = [
    path('sections/', HomeView.as_view(), name='home'),
    path('products/', ProductsView.as_view(), name='products'),
    path('products/<int:pk>/update/', ProductEditView.as_view(), name='products-edit'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='products-delete'),
    path('customers/', CustomerView.as_view(), name='customers'),

]