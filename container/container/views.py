from django.shortcuts import render
from django.db import connections
from django.http import HttpResponse
from datetime import datetime


def home(request): 
    
    current_time = datetime.now().hour # 
    
    greeting = ""
    
    if current_time >= 6 and current_time < 12: 
        greeting = "Good Morning"
    elif current_time >= 12 and current_time < 18: 
        greeting = "Good Afternoon"
    else: 
        greeting = "Good Evening"
        
    return render(request, 'container/index.html', {"logged_in": request.session.get('is_logged_in'), "greeting" : greeting, "name": request.session.get('name')})
