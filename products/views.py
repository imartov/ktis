from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import (Product, Characteristic, ImageProduct,
                     Category, Subcategory)



class CategoryListView(ListView):
    context_object_name = 'category_list'
    queryset = Category.objects.all()
    template_name = 'category_list.html'


class CategoryWIthSubcategoryListDetailView(DetailView):
    context_object_name = 'category'
    model = Category
    template_name = 'category_with_subcategory_list.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['subcategory_list'] = Subcategory.objects.filter(cat=self.get_object())
        return context


class SubcategoryWIthProductsListDetailView(DetailView):
    context_object_name = 'subcategory'
    model = Subcategory
    template_name = 'subcategory_with_products_list.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['products_list'] = Product.objects.filter(subcat=self.get_object())
        return context


class ProductsListView(ListView):
    context_object_name = "products_list"
    queryset = Product.objects.all()
    template_name = 'product_list.html'


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'product_detail.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["characteristics"] = Characteristic.objects.filter(product=self.get_object())
        context["images"] = ImageProduct.objects.filter(product=self.get_object())
        return context
    
