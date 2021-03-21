from django.shortcuts import get_object_or_404, render, get_list_or_404

from .models import Category, Product, Cart

cart = Cart()


def main_page(request):
    categorys = Category.objects.all()
    return render(request, 'shop/main_page.html', {'categorys': categorys})


def product_in_category(request, category_id):
    products = get_list_or_404(Product, category_id=category_id)
    return render(request, 'shop/products.html', {'products': products})


def product(request, category_id, product_id):
    product_info = get_object_or_404(Product, category_id=category_id, id=product_id)
    return render(request, 'shop/product.html', {'product_info': product_info})


def add_to_cart(request, category_id, product_id):
    product = Product.objects.get(category_id=category_id, id=product_id)
    if product.amount == 0:
        raise ValueError("Sorry,we haven't this items anymore")
    product.amount -= 1
    product.save()
    global cart
    cart.save()
    cart.add(product)
    cart.save()
    cost = cart.cost
    return render(request, 'shop/add_to_cart.html', {'cart': cart, 'cost': cost, 'product': product})


def check_cart(request):
    global cart
    cart.save()
    items=cart.product_list.all()
    return render(request, 'shop/cart.html', {'cart': cart, 'items': items})


def checkout(request):
    global cart
    order = cart
    cart.save()
    cart.clear()
    return render(request, 'shop/checkout.html', {'order': order})


def remove_item(request):
    global cart
    try:
        removed = Product.objects.get(id=request.POST["remove"])
        cart.product_list.exclude(product)
        removed.amount += 1
        removed.save()
        cart.cost -= removed.price
        cart.save()
    except Exception:
        return render(request, 'shop/cart_remove.html')
    return render(request, 'shop/cart.html', {'cart': cart})
