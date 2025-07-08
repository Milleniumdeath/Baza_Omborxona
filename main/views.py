from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from datetime import datetime
from .models import *

class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'sections.html')

class ProductsView(LoginRequiredMixin, View):
    def get(self, request):
        products = Products.objects.filter(branch=request.user.branch).order_by('name')
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
            branch=request.user.branch,
        )
        return self.get(request)

class ProductEditView(LoginRequiredMixin, View):
    def get(self, request, pk):
        product = get_object_or_404(Products, pk=pk, branch=request.user.branch)
        context = {
            'product': product,
        }
        return render(request, 'product-edit.html', context)

    def post(self, request, pk):
        product = get_object_or_404(Products, pk=pk, branch=request.user.branch)
        product.name = request.POST.get('name')
        product.brand = request.POST.get('brand')
        product.import_price = request.POST.get('import_price')
        product.export_price = request.POST.get('export_price')
        product.amount = request.POST.get('amount')
        product.unit = request.POST.get('unit')
        product.updated_at=datetime.now()
        product.branch=request.user.branch
        product.save()
        return self.get(request, pk )

class ProductDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        product = get_object_or_404(Products, pk=pk, branch=request.user.branch)
        context = {
            'product': product,
        }
        return render(request, 'product-delete.html', context)
    def post(self, request,pk ):
        product = get_object_or_404(Products, pk=pk)
        product.delete()
        return redirect('products')


class CustomerView(LoginRequiredMixin, View):
    def get(self, request):
        customers = Customer.objects.filter(branch=request.user.branch).order_by('name')
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
            branch=request.user.branch,
        )
        return redirect('customers')

class CustomerEditView(LoginRequiredMixin, View):
    def get(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk, branch=request.user.branch)
        context = {
            'customer': customer,
        }
        return render(request, 'customer-edit.html', context)

    def post(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk, branch=request.user.branch)
        customer.name = request.POST.get('name')
        customer.shop_name = request.POST.get('shop_name')
        customer.phone_number = request.POST.get('phone_number')
        customer.address = request.POST.get('address')
        customer.debt = request.POST.get('debt')
        customer.brand = request.POST.get('brand')
        customer.created_at=datetime.now()
        customer.branch=request.user.branch
        customer.save()
        return self.get(request, pk )

class CustomerDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk, branch=request.user.branch)
        context = {
            'customer': customer,
        }
        return render(request, 'customers-delete.html', context)
    def post(self, request,pk ):
        customer = get_object_or_404(Customer, pk=pk)
        customer.delete()
        return redirect('customers')