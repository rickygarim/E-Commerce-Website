from django.shortcuts import render
from django.db import connections
from django.http import HttpResponse

def info(request):
    return render(request, 'info/index.html', {"logged_in": request.session.get('is_logged_in')})
    