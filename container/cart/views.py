from django.shortcuts import render
from django.db import connections
from django.http import HttpResponse
from store.models import Shopper, Product
from django.contrib import auth
from datetime import datetime


# Create your views here.



def curr_user_to_items(curr_user):
    shopper = Shopper.objects.filter(username=curr_user).first()
    ans = []
    string = str(shopper.items)
    l = string.split(",")
    
    if l[0] == '':
        return []
    if l[-1] == '':
        l.pop()
    return l
    


def print_cart(curr_user):
    curr_cart = curr_user_to_items(curr_user)

    ans = []
    for item in curr_cart:
        thing = Product.objects.filter(id=item)
        wild_books = [thing[0].id, thing[0].name, thing[0].description,
                  thing[0].price, 1 , thing[0].colors_types, thing[0].images]
        
        if wild_books not in ans:
            ans.append(wild_books)
        else: 
            for i in range(len(ans)):
                if int(ans[i][0]) == int(wild_books[0]):
                    ans[i][4] += 1
                    break
    return ans


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
def cart(request):
    logout(request)
            
    if not request.session.get('is_logged_in'):
        request.session['is_logged_in'] = False 
        return render(request, "log/login.html", {"state" : "fromCart", "logged_in": request.session.get('is_logged_in')})
    return render(request, 'cart/index.html', {"rows": print_cart(request.session.get('username'))})