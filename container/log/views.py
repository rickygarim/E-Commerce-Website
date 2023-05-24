from django.shortcuts import render
from django.contrib.auth import authenticate, login
from . models import User
from store.models import Shopper

def login(request):
    if request.method == 'POST': 
        username = request.POST['username']
        password = request.POST['password']
        
        if request.session.get('is_logged_in'): 
            return render(request, 'log/login.html', {"state" : "AlreadyLoggedIn", "logged_in": request.session.get('is_logged_in')})
         
        my_user = User.objects.filter(username=username)

        if len(my_user) == 0: 
            return render(request, 'log/login.html', {"state" : "NoUser", "logged_in": request.session.get('is_logged_in')})
        elif len(my_user) == 1 and my_user[0].password == password: 
            request.session['is_logged_in'] = True
            request.session['username'] = my_user[0].username
            request.session['name'] = my_user[0].first_name
            return render(request, 'log/login.html', {"state" : "Success", "logged_in": request.session.get('is_logged_in')})
        elif my_user[0].password != password: 
            return render(request, 'log/login.html', {"state" : "WrongPassword", "logged_in": request.session.get('is_logged_in')})
        else: 
            return render(request, 'log/login.html', {"state" : "Error", "logged_in": request.session.get('is_logged_in')})
    return render(request, 'log/login.html', {"state" : "", "logged_in": request.session.get('is_logged_in')})
   
    


def logout(request):
    
    if request.session.get('is_logged_in'): 
        request.session['is_logged_in'] = False
        request.session['username'] = ""
        request.session['name'] = ""
        print("went in here!")
        return render(request, 'container/index.html', {"reload": "True"})
    else:
        return render(request, 'log/logout.html', {"state" : "NotLoggedIn"})
        
        


def newUser(request): 
    if request.method == 'POST': 
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        
        my_user = User.objects.filter(username=username)
        
        if len(my_user) == 0: 
            new_user = User(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            new_user.save()
            add_shopper = Shopper(username=username, name=first_name, items="")
            add_shopper.save()
            
            return render(request, 'log/createUser.html', {"state" : "Success"})
        else: 
            return render(request, 'log/createUser.html', {"state" : "UserExists"})
    return render(request, 'log/createUser.html', {"state" : ""})
   