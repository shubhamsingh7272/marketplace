

from django.contrib import admin
from .models import Shop, Product

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'created_at')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'shop', 'created_at')
    list_filter = ('shop',)
    search_fields = ('name', 'shop__name')



# Register your models here.
