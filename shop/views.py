from django.shortcuts import get_object_or_404, render, get_list_or_404
from .models import Category, Product, Cart, ProductPhotos
from django.views.generic import ListView

cart = Cart()


class MainPage(ListView):
    """Get main page with all categories"""
    model = Category
    query_set = Category.objects.all()
    template_name = "shop/main_page.html"


def product_in_category(request, category_pk):
    """Get products list page"""
    products = get_list_or_404(Product, category_id=category_pk)
    return render(request, 'shop/products.html', {'products': products})


def product(request, category_pk, pk):
    """Get product page"""
    product = get_object_or_404(Product, category=category_pk,
                                id=pk)
    photos = ProductPhotos.objects.filter(product_id=pk)
    return render(request, 'shop/product.html', {'product': product,
                                                 'photos': photos})


def add_to_cart(request, category_pk, product_pk):
    """Adding product to cart"""
    adding_product = Product.objects.get(category=category_pk,
                                         id=product_pk)
    if adding_product.amount == 0:
        raise ValueError("Sorry,we haven't this items anymore")
    adding_product.amount -= 1
    adding_product.save()
    global cart
    cart.save()
    cart.add_product_to_cart(adding_product)
    cart.checking_cart_accuracy()
    cart.save()
    cost = cart.cost
    return render(request, 'shop/add_to_cart.html',
                {'cart': cart, 'cost': cost, 'adding_product': adding_product})


def check_cart(request):
    global cart
    cart.save()
    items = cart.product_list.all()
    try:
        removed_product = Product.objects.get(id=request.POST["item"])
        cart.product_list.remove(removed_product)
        removed_product.amount += 1
        removed_product.save()
        cart.cost -= removed_product.price
        cart.save()
        return render(request, 'shop/cart.html', {'cart': cart, 'items': items, 'removed_product': removed_product})
    except Exception:
        return render(request, 'shop/cart.html', {'cart': cart, 'items': items})


def checkout(request):
    global cart
    order = cart
    cart.save()
    cart.clear_cart()
    return render(request, 'shop/checkout.html', {'order': order})
