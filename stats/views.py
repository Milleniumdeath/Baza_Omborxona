from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from django.views import  View
from .models import *
from main.models import *
from django.contrib.auth.mixins import LoginRequiredMixin

class SalesView(LoginRequiredMixin , View):
    def get(self, request):
        sales = Sale.objects.filter(branch=request.user.branch).order_by('-created_at')
        products = Products.objects.filter(branch=request.user.branch).order_by('name')
        customers = Customer.objects.filter(branch=request.user.branch).order_by('name')
        context = {
            'sales': sales,
            'products': products,
            'customers': customers,
        }
        return render(request, 'sales.html', context)

    def post(self, request):
        product = get_object_or_404(Products, id=request.POST['product_id'])
        customer = get_object_or_404(Customer, id=request.POST['customer_id'])
        amount = float(request.POST.get('amount'))
        if amount > product.amount:
            return HttpResponse(
                f"""
                <h2>Mahsulot yetarli emas! Mavjud {product.amount} {product.unit}<br>
                Talab qilingan miqdor: {amount} {product.unit}
                </h2>
                <h2><a href="/stats/sales/">Ortga</a></h2>
                """
            )

        total_price = float(request.POST.get('total_price')) if request.POST.get('total_price') else None


        if  total_price is  None:
            total_price = amount * product.export_price

        paid = float(request.POST.get('paid')) if request.POST.get('paid') else None
        debt = float(request.POST.get('debt')) if request.POST.get('debt') else None

        if  paid is  None and debt is not None:
            paid = total_price - debt
        elif  debt is  None and paid is not None:
            debt = total_price - paid
        else :
                paid = total_price
                debt = 0

        Sale.objects.create(
            product=product,
            customer=customer,
            amount=amount,
            paid=paid,
            debt=debt,
            total_price=total_price,
            branch=request.user.branch,
            user=request.user
        )

        product.amount -= amount
        product.save()

        customer.debt += debt
        customer.save()

        return self.get(request)

class ImportProductsView(LoginRequiredMixin, View):
    def get(self, request):
        import_products = IncomeProduct.objects.filter(branch=request.user.branch).order_by('-created_at')
        products = Products.objects.filter(branch=request.user.branch).order_by('name')
        context = {
            'import_products': import_products,
            'products': products,
        }
        return  render(request, 'import_products.html', context)

    def post(self, request):
        product = get_object_or_404(Products, id=request.POST['product_id'])
        amount = float(request.POST['amount'])
        import_price = float(request.POST.get('import_price'))

        IncomeProduct.objects.create(
            product=product,
            amount=amount,
            import_price=import_price,
            user=request.user,
            branch=request.user.branch,
        )

        product.amount += amount
        product.import_price = import_price
        product.updated_at = datetime.now()
        product.save()
        return self.get(request)



