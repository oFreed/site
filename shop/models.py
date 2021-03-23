from django.db import models
from django.contrib.auth.models import User
from .search import ProductIndex
from django_elastic_appsearch import serialisers
from django_elastic_appsearch.orm import AppSearchModel
from shop.serialisers import CategorySerialiser, ProductSerialiser



class Category(AppSearchModel):
    category_name = models.CharField(max_length=100)

    class AppsearchMeta:
        appsearch_engine_name = 'category'
        appsearch_serialiser_class = CategorySerialiser

    def __str__(self):
        return self.category_name


class Product(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    price = models.PositiveSmallIntegerField(default=0)
    amount = models.PositiveSmallIntegerField(default=0)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    class AppsearchMeta:
        appsearch_engine_name = 'products'
        appsearch_serialiser_class = ProductSerialiser

    def __str__(self):
        return f"model:{self.model} ------- price:{self.price} ---------     amount:{self.amount}"

    def indexing(self):
        obj = ProductIndex(meta={'id': self.id}, brand=self.brand,
                                              model=self.model, price=self.price, amount=self.amount, category_id=self.category_id_id)
        obj.save()
        return obj.to_dict(include_meta=True)


class Cart(models.Model):
    product_list = models.ManyToManyField(Product, default=1)
    cost = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def add(self, product):
        if product.price < 0:
            product.price = product.price * -1
        self.product_list.add(product.id)
        self.cost += product.price

    def clear(self):
        self.product_list.clear()
        self.cost = 0

    def __str__(self):
        list = ",".join([str(i.model) for i in self.product_list.all()])
        for i in self.product_list.all():
            self.cost+=i.price
        return f"Item in your cart is: {list} and it cost {self.cost}₴"


