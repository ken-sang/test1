from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render

def home(request):
    context = {}  # Fixed the typo from contetx to context
    return render(request, 'app2/home.html', context)  # Correct indentation and context variable

def cart(request):
    context = {}  # Fixed the typo from contetx to context
    return render(request, 'app2/cart.html', context)  # Correct file path and context variable

def checkout(request):  # Fixed the typo in function name from checkuot to checkout
    context = {}  # Fixed the typo from contetx to context
    return render(request, 'app2/checkout.html', context)  # Correct file path and context variable
