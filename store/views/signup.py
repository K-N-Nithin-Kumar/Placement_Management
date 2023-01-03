from django.shortcuts import render, redirect
from store.models.customer import Student
from django.contrib.auth.hashers import make_password , check_password
from django.views import View

#print(make_password('1234'))
#print(check_password('1234','pbkdf2_sha256$320000$iFlCjCnHS2k3PDU2oZcNZC$YM7bzL1OIBcMX6tdqBHwk2mu7NJtZOV4vh/Hxz7ljUs='))
class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postdata = request.POST
        first_name = postdata.get('firstname')
        last_name = postdata.get('lastname')
        email = postdata.get('email')
        phone = postdata.get('phone')
        password = postdata.get('password')
        cgpa =postdata.get('cgpa')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        customer = Student(first_name=first_name, last_name=last_name, phone=phone, email=email, password=password,cgpa=cgpa)
        error_message = self.validateStudent(customer)
        if not error_message:
            print(first_name, last_name, email, password)
            customer.password = make_password(customer.password)
            customer.register()

            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validateStudent(self, customer):
        error_message = None
        if not customer.first_name:
            error_message = "First Name Required!!"
        elif len(customer.first_name) < 4:
            error_message = "First name must be 4 characters long"
        elif not customer.last_name:
            error_message = "Last Name Required!!"
        elif len(customer.first_name) < 4:
            error_message = "Last name must be 4 characters long"
        elif not customer.phone:
            error_message = "Phone number Required!!"
        elif len(customer.phone) < 10:
            error_message = "phone number must be 10 characters long"
        elif not customer.email:
            error_message = "email required"
        elif len(customer.email) < 2:
            error_message = "give the proper email"
        elif customer.isExists():
            error_message = "Email address is already exists"
        return error_message
