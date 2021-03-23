from django.urls import path

from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('<category_id>/', views.product_in_category, name='product_in_category'),
    path('<category_id>/<product_id>/', views.product, name='product'),
    path('<category_id>/<product_id>/cart/', views.add_to_cart, name='add_to_cart'),
    path('/cart/', views.check_cart, name='check_cart'),
    path('/cart/remove', views.remove_item, name='remove_item'),
    path('/cart/checkout/', views.checkout, name='checkout'),
]
