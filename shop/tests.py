from django.test import TestCase
from .models import Product, Cart, Category

product=Product.objects.get(id=1)

# class ProductCheck(TestCase):
#     def test_validation_of_price(self):
#         self.assertGreaterEqual(product.price,0)
#
#     def test_validation_of_amount(self):
#         self.assertGreaterEqual(product.amount,0)


class CartCheck(TestCase):

    def test_cart_valid(self):
        cart=Cart()
        cart.save()
        cart.add(product)
        cart.save()
        self.assertGreaterEqual(cart.cost,0)



