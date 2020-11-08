from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list),
    path('product-form/', views.product_form),
    path('category-form/', views.category_form)
]