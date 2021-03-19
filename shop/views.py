from django.shortcuts import get_object_or_404, render ,get_list_or_404

from .models import Category,Product

cart=[]
cost=0

def main_page(request):
    categorys=Category.objects.all()
    return render(request, 'shop/main_page.html', {'categorys': categorys})


def product_in_category(request, category_id):
    products = get_list_or_404(Product,category_id=category_id)
    return render(request, 'shop/products.html', {'products': products})


def product(request,category_id,product_id):
    product_info = get_object_or_404(Product,category_id=category_id,id=product_id)
    return render(request, 'shop/product.html', {'product_info': product_info})


def add_to_cart(request,category_id,product_id):
    product = Product.objects.get(category_id=category_id,id=product_id)
    global cart,cost
    cart.append(product)
    cost+=product.price
    return render(request,'shop/cart.html',{'cart' : cart,'product' : product,'cost':cost })


def check_cart(request):
    return render(request,'shop/cart.html',{'cart' : cart,'product' : product,'cost':cost })




