from django.shortcuts import render
from store.models.orders import Order
from django.views import View


# from store.middleware.auth import auth_middleware
# from django.utils.decorators import method_decorator

# Fetch Data To Show In the Cart Page
class OrderView(View):
    # @method_decorator(auth_middleware)
    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        return render(request, 'orders.html', {'orders': orders})
