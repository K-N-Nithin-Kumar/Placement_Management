from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Student
from django.views import View

from store.models.product import Company
from store.models.orders import Application
from store.middlewares.auth import auth_middleware

class OrderView(View):


    def get(self , request ):
        customer = request.session.get('customer')
        orders = Application.get_orders_by_customer(customer)
        print(orders)
        return render(request , 'orders.html'  , {'orders' : orders})