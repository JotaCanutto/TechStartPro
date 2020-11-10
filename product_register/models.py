"""Models"""
from django.db import models

# Create your models here.


class Category(models.Model):
    """Classe Categoria"""
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Product(models.Model):
    """Classe Produto"""
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.CharField(max_length=20)
    category = models.ManyToManyField(Category)

    def is_in_stock(self):
        """Função para testar a classe Produto"""
        return self.name is not None
