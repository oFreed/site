from django.urls import path

from . import views
urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('<category_id>', views.product_in_category,name='product_in_category'),
    path('<category_id>/<product_id>/', views.product,name='product'),
]