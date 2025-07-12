from django.db import models
from django.contrib.auth.models import AbstractUser
from main.models import *


class User(AbstractUser):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, blank=True, null=True)
    phone_number = models.CharField(max_length=13, blank=True, null=True)

    class Meta:
        verbose_name = "Xodim"
        verbose_name_plural = "Xodimlar"