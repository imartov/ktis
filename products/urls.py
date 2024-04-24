from django.urls import path

from .views import (ProductDetailView, ProductsListView,
                    CategoryWIthSubcategoryListDetailView,
                    SubcategoryWIthProductsListDetailView,
                    CategoryListView)

urlpatterns = [
    # Category
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('category/<slug:slug>', CategoryWIthSubcategoryListDetailView.as_view(), name='category_detail'),
    
    # Subcategory
    path('subcategory/<slug:slug>', SubcategoryWIthProductsListDetailView.as_view(), name='subcategory_detail'),

    # Product
    path('products/', ProductsListView.as_view(), name='product_list'),
    path('product/<slug:slug>', ProductDetailView.as_view(), name='product_detail'),
]