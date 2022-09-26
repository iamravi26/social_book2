
from django.db import models

# Create your models here.

class user(models.Model):
    name=models.CharField(max_length=150)
    username=models.CharField(max_length=150)
    email=models.EmailField(max_length=150)
    password=models.CharField(max_length=150)

