from django.db import models
from django.contrib.auth.models import AbstractUser
from main.models import *


class User(AbstractUser):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=13)
