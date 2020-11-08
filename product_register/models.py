from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 20)

class Product(models.Model):
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100)
    price = models.CharField(max_length = 20)
    category = models.ManyToManyField(Category)