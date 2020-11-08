from django.shortcuts import render
from .forms import ProductForm

# Create your views here.

def product_list(request):
    return render(request, "product_register/product_list.html")

def product_form(request):
    form = ProductForm()
    return render(request, "product_register/product_form.html", {'form':form})

def category_form(request):
    return render(request, "product_register/category_form.html")

def product_delete(request):
    return