from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from store.models.product import Product
from django.views import View


# Fetch Data To Show In the Cart Page
class Cart(View):
    def get(self, request):
        ids = request.session.get('cart').keys()
        products = Product.get_products_by_id(ids)
        # print(products)
        return render(request, 'cart.html', {'products': products})
