from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name


class Product(models.Model):
    """Product model"""
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    price = models.PositiveSmallIntegerField(default=0)
    amount = models.PositiveSmallIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.brand} {self.model}"

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def checking_product_accuracy(self):
        """Checking price and amount for accuracy"""
        if self.price < 0:
            self.price = abs(self.price)
        if self.amount < 0:
            self.amount = abs(self.amount)
        return self.price, self.amount


class ProductPhotos(models.Model):
    """Photos for our products"""
    image = models.ImageField(upload_to='', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Product photo"
        verbose_name_plural = "Product photos"

    def __str__(self):
        return f"Photo for {self.product.brand} {self.product.model}"


class Cart(models.Model):
    """Users cart"""
    product_list = models.ManyToManyField(Product)
    cost = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"

    def add_product_to_cart(self, product):
        """Adding product to the cart"""
        if product.price < 0:
            product.price = abs(product.price)
        self.product_list.add(product.id)
        self.cost += product.price

    def clear_cart(self):
        """Delete all items from the cart"""
        self.product_list.clear()
        self.cost = 0

    def __str__(self):
        list_of_products = ",".join([str(i.model) for i in self.product_list.all()])
        for i in self.product_list.all():
            self.cost += i.price
        return f"Item in {self.user}'s cart is:{list_of_products} and it cost {self.cost}₴"

    def checking_cart_accuracy(self):
        """Checking price and amount for accuracy"""
        if self.cost < 0:
            self.cost = abs(self.cost)
