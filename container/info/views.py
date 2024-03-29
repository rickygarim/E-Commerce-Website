from django.shortcuts import render
from django.db import connections
from django.http import HttpResponse
from datetime import datetime

def get_datetime_number():
    now = datetime.now()
    datetime_number = now.strftime('%Y%m%d%H%M%S')
    return int(datetime_number)

def logout(request): 
    if bool(request.session.get("is_logged_in")) and (get_datetime_number() - int(request.session.get('logged_in_time')) >= 10000):
        if not bool(request.session.get('remember_me')):
            request.session['is_logged_in'] = False 
            request.session['remember_me'] = False 
            return render(request, 'log/login.html', {"state": "Session Timed out", "logged_in": request.session.get('is_logged_in')})
        elif get_datetime_number() - int(request.session.get('logged_in_time')) >= 1000000: 
            request.session['is_logged_in'] = False 
            request.session['remember_me'] = False 
            return render(request, 'log/login.html', {"state": "Session Timed out", "logged_in": request.session.get('is_logged_in')})
        
def info(request):
    logout(request)
    return render(request, 'info/index.html', {"logged_in": request.session.get('is_logged_in')})
    