from django.shortcuts import render
from django.contrib.auth import authenticate, login
from . models import User
from store.models import Shopper
from django.shortcuts import redirect
from datetime import datetime

def get_datetime_number():
    now = datetime.now()
    datetime_number = now.strftime('%Y%m%d%H%M%S')
    return int(datetime_number)

def login(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        remember= request.POST.get('remember')
        
        if request.session.get('is_logged_in'):
            return render(request, 'log/login.html', {"state": "AlreadyLoggedIn", "logged_in": request.session.get('is_logged_in')})

        my_user = User.objects.filter(username=username)

        if len(my_user) == 0:
            return render(request, 'log/login.html', {"state": "NoUser", "logged_in": request.session.get('is_logged_in')})
        elif len(my_user) == 1 and my_user[0].password == password:
            request.session['is_logged_in'] = True
            request.session['username'] = my_user[0].username
            request.session['name'] = my_user[0].first_name
            request.session['logged_in_time'] = get_datetime_number()
            request.session['remember_me'] = bool(remember)
            
            return redirect('home')
        elif my_user[0].password != password:
            return render(request, 'log/login.html', {"state": "WrongPassword", "logged_in": request.session.get('is_logged_in')})
        else:
            return render(request, 'log/login.html', {"state": "Error", "logged_in": request.session.get('is_logged_in')})
    return render(request, 'log/login.html', {"state": "", "logged_in": request.session.get('is_logged_in')})


def auto_login(request, username, password):
    my_user = User.objects.filter(username=username)
    request.session['is_logged_in'] = True
    request.session['username'] = my_user[0].username
    request.session['name'] = my_user[0].first_name
    
    return redirect('home')
   

def logout(request):

    if request.session.get('is_logged_in'):
        request.session['is_logged_in'] = False
        request.session['username'] = ""
        request.session['name'] = ""
        return redirect('/log/login')
    else:
        return render(request, 'log/login.html', {"state": "NotLoggedIn"})


def newUser(request):
   
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        re_password = request.POST['re-password']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        if password != re_password:
            return render(request, 'log/createUser.html', {"state": "PasswordMismatch", "logged_in": request.session.get('is_logged_in')})
        my_user = User.objects.filter(username=username)
        my_user_email = User.objects.filter(email=email)
        if len(my_user) == 0 and len(my_user_email) == 0:
            new_user = User(username=username, password=password,
                            email=email, first_name=first_name, last_name=last_name)
            new_user.save()
            add_shopper = Shopper(username=username, name=first_name, items="")
            add_shopper.save()

            return auto_login(request, username, password)
        else:
            if len(my_user) > 0:
                return render(request, 'log/createUser.html', {"state": "UserExists", "logged_in": request.session.get('is_logged_in')})
            elif len(my_user_email) > 0:
                return render(request, 'log/createUser.html', {"state": "EmailExists", "logged_in": request.session.get('is_logged_in')})
    return render(request, 'log/createUser.html', {"state": "", "logged_in": request.session.get('is_logged_in')})
