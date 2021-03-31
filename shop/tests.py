from django.test import TestCase
from .models import Product, Cart
from django.urls import reverse


product = Product(price=-300, amount=-6)


class ProductCheck(TestCase):
    """Checking product accuracy"""
    product.checking_product_accuracy()

    def test_validation_of_price(self):
        self.assertGreaterEqual(product.price, 0)

    def test_validation_of_amount(self):
        self.assertGreaterEqual(product.amount, 0)


class CartCheck(TestCase):
    """Checking cart accuracy"""
    def test_cost_validation(self):
        cart = Cart(cost=-55)
        cart.checking_cart_accuracy()
        self.assertGreaterEqual(cart.cost, 0)


class LinksTest(TestCase):
    """Checking work of links"""
    """Checking main page"""
    def test_main_page(self):
        response = self.client.get(reverse('shop:main_page'))
        self.assertEqual(response.status_code, 200)

    """Checking removing page"""
    def test_product_in_category(self):
        response = self.client.get(reverse('shop:remove_item'))
        self.assertEqual(response.status_code, 200)
