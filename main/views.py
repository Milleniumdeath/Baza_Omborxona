
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from datetime import datetime
from .models import *

class HomeView(View):
    def get(self, request):
        return render(request, 'sections.html')

class ProductsView(View):
    def get(self, request):
        products = Products.objects.order_by('name')
        context = {
            'products': products,
        }

        return render(request, 'products.html', context)

    def post(self, request):
        Products.objects.create(
            name=request.POST.get('name'),
            brand=request.POST.get('brand') if request.POST.get('brand') != "" else None,
            import_price=request.POST.get('import_price'),
            export_price=request.POST.get('export_price') if request.POST.get('export_price') != "" else None,
            amount=request.POST.get('amount'),
            unit=request.POST.get('unit'),
            updated_at=datetime.now(),
        )
        return self.get(request)

class ProductEditView(View):
    def get(self, request, pk):
        product = get_object_or_404(Products, pk=pk)
        context = {
            'product': product,
        }
        return render(request, 'product-edit.html', context)

    def post(self, request, pk):
        product = get_object_or_404(Products, pk=pk)
        product.name = request.POST.get('name')
        product.brand = request.POST.get('brand')
        product.import_price = request.POST.get('import_price')
        product.export_price = request.POST.get('export_price')
        product.amount = request.POST.get('amount')
        product.unit = request.POST.get('unit')
        product.updated_at=datetime.now()
        product.save()
        return self.get(request, pk )

class ProductDeleteView(View):
    def get(self, request, pk):
        product = get_object_or_404(Products, pk=pk)
        context = {
            'product': product,
        }
        return render(request, 'product-delete.html', context)
    def post(self, request,pk ):
        product = get_object_or_404(Products, pk=pk)
        product.delete()
        return redirect('products')


class CustomerView(View):
    def get(self, request):
        customers = Customer.objects.order_by('name')
        context = {
            'customers': customers,
        }

        return render(request, 'customers.html', context)

    def post(self, request):
        Customer.objects.create(
            name=request.POST.get('name'),
            shop_name=request.POST.get('shop_name'),
            phone_number=request.POST.get('phone_number'),
            address=request.POST.get('address'),
            debt=request.POST.get('debt'),
            brand=request.POST.get('brand'),
            created_at=datetime.now(),
        )
        return redirect('customers')
