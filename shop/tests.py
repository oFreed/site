from django.test import TestCase
from .models import Product, Cart
from django.urls import reverse

product = Product(price=-300, amount=-6)


class ProductCheck(TestCase):
    product.checking()

    def test_validation_of_price(self):
        self.assertGreaterEqual(product.price, 0)

    def test_validation_of_amount(self):
        self.assertGreaterEqual(product.amount, 0)


class CartCheck(TestCase):

    def test_cost_validation(self):
        cart = Cart(cost=-55)
        cart.cart_check()
        self.assertGreaterEqual(cart.cost, 0)


class LinksTest(TestCase):

    def test_main_page(self):
        response = self.client.get(reverse('shop:main_page'))
        self.assertEqual(response.status_code, 200)
