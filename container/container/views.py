from django.shortcuts import render
from django.db import connections
from django.http import HttpResponse
from datetime import datetime


def get_datetime_number():
    now = datetime.now()
    datetime_number = now.strftime('%Y%m%d%H%M%S')
    return int(datetime_number)

def capitalize(name):
    return name[0].upper() + name[1:]
    


def home(request): 
    if request.session.get("is_logged_in") and (get_datetime_number() - request.session.get('logged_in_time') >= 10000):
        if not request.session.get('remember_me'):
            request.session['is_logged_in'] = False 
            return render(request, 'log/login.html', {"state": "Session Timed out", "logged_in": request.session.get('is_logged_in')})
        elif get_datetime_number() - request.session.get('logged_in_time') >= 1000000: 
            request.session['is_logged_in'] = False 
            return render(request, 'log/login.html', {"state": "Session Timed out", "logged_in": request.session.get('is_logged_in')})
    
    current_time = datetime.now().hour # 
    greeting = ""
    if current_time >= 6 and current_time < 12: 
        greeting = "Good Morning"
    elif current_time >= 12 and current_time < 18: 
        greeting = "Good Afternoon"
    else: 
        greeting = "Good Evening"
    
    if not request.session.get('is_logged_in'):
        return render(request, 'container/index.html', {"logged_in": "False", "greeting" : greeting})
    return render(request, 'container/index.html', {"logged_in": str(request.session.get('is_logged_in')), "greeting" : greeting, "name": capitalize(request.session.get('name'))})
