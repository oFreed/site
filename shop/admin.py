from django.contrib import admin
from .models import Category, Product, Cart, ProductPhotos


class ProductPhotosInline(admin.StackedInline):
    """To add a few photos in a time"""
    model = ProductPhotos
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    """Changing Product table,adding filters and search at admin site"""
    fieldsets = [
        ("Product's category", {'fields': ['category']}),
        ("Product's info", {'fields': ['brand', 'model', 'price', 'amount']})
    ]
    inlines = [ProductPhotosInline]
    list_display = ('brand', 'category', 'model', 'price', 'amount')
    list_filter = ['category', 'brand']
    search_fields = ['model', 'brand', 'category']


class ProductPhotosAdmin(admin.ModelAdmin):
    """Changing ProductPhotos table and add some filters at admin site"""
    fieldsets = [
        ('Photo belongs', {'fields': ['product']}),
        ("Photo's file", {'fields': ['image']})
    ]
    list_filter = ['product']


class CartAdmin(admin.ModelAdmin):
    """Changing Cart table at admin site"""
    fieldsets = [
        ('Cart belongs', {'fields': ['user']}),
        ('Cart info', {'fields': ['product_list', 'cost']})
    ]
    list_display = ('user', 'cost')


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductPhotos, ProductPhotosAdmin)
admin.site.register(Cart, CartAdmin)
