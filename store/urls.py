from django.contrib import admin
from django.urls import path
from .views.index import Index
from .views.signup import Signup
from .views.login import Login, logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .middleware.auth import auth_middleware
from .views import index, login, signup

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('signup', Signup.as_view(), name="signup"),
    path('login', Login.as_view(), name="login"),
    path('logout', logout, name="logout"),
    path('cart', Cart.as_view(), name="cart"),
    path('check-out', CheckOut.as_view(), name="checkout"),
    path('orders', auth_middleware(OrderView.as_view()), name="orders")

    # Route For Login  and Registration Functional Method
    # path('login', views.login, name="login")
    # path('signup', views.signup, name="signup"),
]
