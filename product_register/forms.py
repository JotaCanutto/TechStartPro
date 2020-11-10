"""Formulários"""
from django import forms
from .models import Product, Category

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

class CategoryUpload(forms.ModelForm):
    """Upload de Categorias"""
    class Meta:
        model = Category
        fields = "__all__"
