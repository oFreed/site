from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    price = models.PositiveSmallIntegerField(default=0)
    amount = models.PositiveSmallIntegerField(default=0)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    def checking(self):
        if self.price < 0:
            self.price = abs(self.price)
        if self.amount < 0:
            self.amount = abs(self.amount)
        return self.price, self.amount

    def __str__(self):
        return f"model:{self.model} ------- price:{self.price} ---------     amount:{self.amount}"


class ProductPhotos(models.Model):
    image = models.ImageField(upload_to='', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for {self.product}"


class Cart(models.Model):
    product_list = models.ManyToManyField(Product)
    cost = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def add(self, product):
        if product.price < 0:
            product.price = abs(product.price)
        self.product_list.add(product.id)
        self.cost += product.price

    def clear(self):
        self.product_list.clear()
        self.cost = 0

    def __str__(self):
        list = ",".join([str(i.model) for i in self.product_list.all()])
        for i in self.product_list.all():
            self.cost += i.price
        return f"Item in {self.user}'s cart is: {list} and it cost {self.cost}₴                                       m"

    def cart_check(self):
        if self.cost < 0:
            self.cost = abs(self.cost)
