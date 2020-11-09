"""Formulários"""
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    """Formulário de Produto"""
    class Meta:
        model = Product
        fields = ('name','description','price','category')
        labels = {
            'name':'Nome',
            'description':'Descrição',
            'price':'Preço',
            'category':'Categoria'
        }
