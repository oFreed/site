from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"model:{self.model} ------- price:{self.price} ---------     amount:{self.amount}"


class Cart(models.Model):
    product_list = models.ManyToManyField(Product, blank=True)
    cost = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def add(self, product):
        self.product_list.add(product.id)
        self.cost += product.price

    def clear(self):
        self.product_list.clear()
        self.cost = 0

    def __str__(self):
        list = ",".join([str(i.model) for i in self.product_list.all()])
        return f"Item in your cart is: {list} and it cost {self.cost}₴"
