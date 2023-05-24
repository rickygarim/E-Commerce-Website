from django.shortcuts import render
from django.db import connections
from django.http import HttpResponse

def home(request):
    return render(request, 'container/index.html', {"logged_in": request.session.get('is_logged_in'), "reload": False})