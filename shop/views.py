from django.shortcuts import render, redirect
from .models import Shop
from django.http import HttpResponse
from .models import Product
def add_shop(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        address = request.POST.get('address')
        shop = Shop.objects.create(name=name, description=description, address=address)
        return redirect('shop_list')  # Redirect to the shop list view

    return render(request, 'shop/add_shop.html')


def add_product(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        shop_id = request.POST.get('shop')
        shop = Shop.objects.get(id=shop_id)
        Product.objects.create(name=name, description=description, price=price, shop=shop)
        return redirect('shop_list')  # Redirect to the shop list view

    shops = Shop.objects.all()
    return render(request, 'shop/add_product.html', {'shops': shops})


def shop_list(request):
    shops = Shop.objects.prefetch_related('products').all()
    return render(request, 'shop/shop_list.html', {'shops': shops})
