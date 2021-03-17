from django.shortcuts import get_object_or_404, render
from django.http import Http404

from .models import Category,Product

def main_page(request):
    categorys=Category.objects.all()
    return render(request, 'shop/main_page.html', {'categorys': categorys})

def product_in_category(request, category_id):
    products = Product.objects.filter(category_id=category_id)
    return render(request, 'shop/products.html', {'products': products})

def product(request,product):
    product=Product.objects.filter(product_id=product)
    return render(request, 'shop/product.html', {'product': product})


