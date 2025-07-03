from django.core.validators import MinValueValidator
from django.db import models

class Branch(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255, blank=True, null=True)
    import_price = models.FloatField(validators=[MinValueValidator(0.0)])
    export_price = models.FloatField(validators=[MinValueValidator(0.0)], blank=True, null=True)
    amount = models.FloatField(validators=[MinValueValidator(0.0)])
    unit = models.CharField(max_length=255, blank=True, null=True)
    crated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=255)
    shop_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=13, blank=True, null=True)
    address = models.TextField()
    debt = models.FloatField(validators=[MinValueValidator(0.0)], default=0)
    crated_at = models.DateTimeField(auto_now_add=True)
    brand = models.CharField(max_length=255, blank=True, null=True)

