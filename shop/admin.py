from django.contrib import admin
from .models import Category, Product, Cart, ProductPhotos

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductPhotos)
admin.site.register(Cart)
