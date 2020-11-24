from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from store.models.customer import Customer
from django.views import View


# Login According To class Based View To follow get and Post Method
class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                return redirect('index')
            else:
                error_message = 'Email or Password is Invalid'
        else:
            error_message = 'Email or Password is Invalid'
        return render(request, 'login.html', {'error': error_message})

def logout(request):
    request.session.clear()
    return redirect('login')
# Login According to the object method Regular Practices in Daily life
# def login(request):
#     if request.method == 'GET':
#         return render(request, 'login.html')
#     else:
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         customer = Customer.get_customer_by_email(email)
#         error_message = None
#         if customer:
#             flag = check_password(password, customer.password)
#             if flag:
#                 return redirect('index')
#             else:
#                 error_message = 'Email or Password is Invalid'
#         else:
#             error_message = 'Email or Password is Invalid'
#         return render(request, 'login.html', {'error': error_message})
