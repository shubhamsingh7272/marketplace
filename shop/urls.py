from django.urls import path
from . import views

urlpatterns = [
    path('add-shop/', views.add_shop, name='add_shop'),
    path('add-product/', views.add_product, name='add_product'),
    path('', views.shop_list, name='shop_list'),
]
