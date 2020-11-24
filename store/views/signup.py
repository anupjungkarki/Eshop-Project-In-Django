from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from store.models.customer import Customer
from django.views import View


# def validateCustomer(customer):
#     #  Form Validations Code
#     error_message = None
#     if not customer.first_name:
#         error_message = "First Name is Require!!"
#     elif customer.first_name:
#         if len(customer.first_name) < 4:
#             error_message = "First Name Must be 4 Character Long"
#
#     if not customer.last_name:
#         error_message = "Last Name is Require!!"
#     elif customer.last_name:
#         if len(customer.last_name) < 4:
#             error_message = "Last Name is Required!!"
#
#     if not customer.phone:
#         error_message = "Phone Number is Require!!"
#     elif customer.phone:
#         if len(customer.phone) < 10:
#             error_message = "Phone Number Should be 10 Digit"
#
#     elif len(customer.password) < 8:
#         error_message = "Password Must Be 8 Character Long"
#
#     if not customer.email:
#         error_message = "Email Field is Require!!"
#     elif len(customer.email) < 9:
#         error_message = "Email Must Be 9 Character Long"
#
#     elif customer.isExists():
#         error_message = "Email Address Already Register"
#     return error_message
#
#
# def registerUser(request):
#     postData = request.POST
#     first_name = postData.get('firstname')
#     last_name = postData.get('lastname')
#     phone = postData.get('phone')
#     email = postData.get('email')
#     password = postData.get('password')
#
#     # Show Last InputField Values Dictonary  Talako Values Bhitra  Bhako
#     values = {
#         'first_name': first_name,
#         'last_name': last_name,
#         'phone': phone,
#         'email': email
#     }
#     customer = Customer(first_name=first_name,
#                         last_name=last_name,
#                         phone=phone,
#                         email=email,
#                         password=password)
#     error_message = validateCustomer(customer)
#
#     # print(first_name, last_name, phone, email, password)
#     # Saving Data To Database
#     if not error_message:
#         # Convert Password To Hash Fromate
#         customer.password = make_password(customer.password)
#         customer.register()
#         return redirect('index')
#     else:
#         data = {
#             'error': error_message,
#             'value': values
#         }
#         return render(request, 'signup.html', data)
#
# def signup(request):
#     if request.method == 'GET':
#         return render(request, 'signup.html')
#     else:
#         return registerUser(request)


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        # Show Last InputField Values Dictonary  Talako Values Bhitra  Bhako
        values = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)
        error_message = self.validateCustomer(customer)

        # print(first_name, last_name, phone, email, password)
        # Saving Data To Database
        if not error_message:
            # Convert Password To Hash Format
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('index')
        else:
            data = {
                'error': error_message,
                'value': values
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        #  Form Validations Code
        error_message = None
        if not customer.first_name:
            error_message = "First Name is Require!!"
        elif customer.first_name:
            if len(customer.first_name) < 4:
                error_message = "First Name Must be 4 Character Long"

        if not customer.last_name:
            error_message = "Last Name is Require!!"
        elif customer.last_name:
            if len(customer.last_name) < 4:
                error_message = "Last Name is Required!!"

        if not customer.phone:
            error_message = "Phone Number is Require!!"
        elif customer.phone:
            if len(customer.phone) < 10:
                error_message = "Phone Number Should be 10 Digit"

        elif len(customer.password) < 8:
            error_message = "Password Must Be 8 Character Long"

        if not customer.email:
            error_message = "Email Field is Require!!"
        elif len(customer.email) < 9:
            error_message = "Email Must Be 9 Character Long"

        elif customer.isExists():
            error_message = "Email Address Already Register"
        return error_message
