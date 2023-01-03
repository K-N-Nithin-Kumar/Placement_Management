from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Student
from django.views import View
from store.models.product import Company
from datetime import datetime

class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Company.get_products_by_id(ids)
        print(products)
        return render(request, 'cart.html', {'products': products})
    
  
