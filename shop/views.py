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
    if product.amount == 0:
        raise ValueError("Sorry,we haven't this items anymore")
    product.amount -= 1
    product.save()
    global cart,cost
    cart.append(product)
    cost+=product.price
    return render(request,'shop/cart.html',{'cart' : cart,'product' : product,'cost':cost })


def check_cart(request):
    return render(request,'shop/cart.html',{'cart' : cart,'product' : product,'cost':cost })


def checkout(request):
    global cart,cost
    order = cart
    cart=[]
    cost=0
    return render(request,'shop/checkout.html',{'cart' : cart,'order' : order})

def remove_item(request):
    global cart
    try:
        new=Product.objects.get(id=request.POST["remove"])
        cart.remove(new)
        new.amount+=1
        new.save()
    except(ProductDoesNotExist):
        new=[1,2]
    return render(request,'shop/cart.html',{'cart' : cart,'new':new})


