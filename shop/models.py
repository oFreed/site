from django.db import models

class Category(models.Model):
    category_name=models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return f"model:{self.model} ------- price:{self.price} ---------     amount:{self.amount}"




