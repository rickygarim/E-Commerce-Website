from django.shortcuts import render
from django.db import connections
from django.http import HttpResponse
from store.models import Shopper, Product
from django.contrib import auth



# Create your views here.


def curr_user_to_items(curr_user):
    shopper = Shopper.objects.filter(username=curr_user).first()
    ans = []
    print(str(shopper.items))
    for i in range(len(str(shopper.items))):
        if shopper.items[i] == ',':
            ans.append(shopper.items[:i])
            shopper.items = shopper.items[i+1:]
    return ans


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
                if ans[i][0] == wild_books[0]:
                    ans[i][4] += 1
                    break
    return ans


def cart(request):
    if not request.session.get('is_logged_in'):
        return render(request, "log/logout.html", {"state": "NotLoggedIn", "from": "cart"})
    auth
    return render(request, 'cart/index.html', {"logged_in": request.session.get('is_logged_in'), "username":  request.session.get('username'), "cart": print_cart(request.session.get('username'))})
