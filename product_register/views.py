"""Views"""
import io
import csv
from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product, Category

# Create your views here.


def product_list(request):
    """Lista de Produtos"""
    context = {'product_list': Product.objects.all()}
    return render(request, "product_register/product_list.html", context)


def product_form(request, product_id=0):
    """Formulário de Cadastro de Produtos"""
    if request.method == "GET":
        if product_id == 0:
            form = ProductForm()
        else:
            product = Product.objects.get(pk=product_id)
            form = ProductForm(instance=product)
        return render(request, "product_register/product_form.html", {'form': form})
    else:
        if product_id == 0:
            form = ProductForm(request.POST)
        else:
            product = Product.objects.get(pk=product_id)
            form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
        return redirect('/product')


def category_form(request):
    """Cadastro de Categorias"""
    if request.method == "GET":
        return render(request, "product_register/category_form.html")
    else:
        #CSV UPLOAD HERE
        csv_file =  request.FILES['file']
        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)
        for column in csv.reader(io_string, delimiter=','):
            _, created = Category.objects.update_or_create(
                name = column[0],
            )
        return redirect('/product')


def product_delete(request, product_id=0):
    """Exclusão de Produtos"""
    product = Product.objects.get(pk=product_id)
    product.delete()
    return redirect('/product')
