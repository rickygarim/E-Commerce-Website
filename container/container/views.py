from django.shortcuts import render
from django.db import connections
from django.http import HttpResponse

def home(request):
    return render(request, 'container/index.html')