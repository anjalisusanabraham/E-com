from django.shortcuts import render

# Create your views here.

def customer_home(request):
    return render(request,'customer_template/customerhome.html')


def display_cart(request):
    return render(request,'customer_template/cart.html')