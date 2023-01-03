from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Student
from django.views import View

from store.models.product import Company
from store.models.orders import Application


class CheckOut(View):
    def post(self, request):
        profile = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Company.get_products_by_id(list(cart.keys()))
        # print(address, phone, customer, cart, products)

        for product in products:
            print(cart.get(str(product.id)))
            order = Application(customer=Student(id=customer),
                          product=product,
                          price=product.cgpa,
                          profile=profile,
                          phone=phone,
                        #   quantity=cart.get(str(product.id)))
            )
            order.save()
        request.session['cart'] = {}

        return redirect('cart')