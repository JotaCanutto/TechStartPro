"""Urls"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product-form/', views.product_form, name='product_insert'),
    path('product-form/<int:product_id>/', views.product_form, name='product_update'),
    path('product-form/delete/<int:product_id>/', views.product_delete, name='product_delete'),
    path('category-form/', views.category_form, name='category_insert')
]
