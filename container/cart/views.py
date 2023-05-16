from django.shortcuts import render
from django.db import connections
from django.http import HttpResponse

def cart(request):
    return render(request, 'cart/index.html')