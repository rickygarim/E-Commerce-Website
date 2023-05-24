from django.shortcuts import render
from . models import Product, Shopper
from django.db import connections


def store(request):
    all_products = Product.objects.all()
    context = []
    for thing in all_products:
        if thing.quantity > 0:
            context.append([thing.id, thing.name, thing.description,
                           thing.price, thing.quantity, thing.colors_types, thing.images])
    return render(request, 'store/index.html', {"rows": context, "logged_in": request.session.get('is_logged_in')})


def item(request, item_id):
    thing = Product.objects.filter(id=item_id)
    wild_books = [thing[0].id, thing[0].name, thing[0].description,
                  thing[0].price, thing[0].quantity, thing[0].colors_types, thing[0].images]
    return render(request, 'store/item.html', {'row':  wild_books, "logged_in": request.session.get('is_logged_in')})


def add_item_here(number, username):
    shopper = Shopper.objects.filter(username=username).first()
    if shopper is not None:
        shopper.items += str(number) + ','
        shopper.save()
        
    
    


def add_to_cart(request, item_name):
    if request.session.get('is_logged_in'):
        all_data = Product.objects.filter(id=item_name)
        item = all_data[0]

        if item.quantity <= 0:
            return render(request, 'store/cart.html', {"no_stock": "TRUE", item: "", "logged_in": request.session.get('is_logged_in')})
        else:
            item.quantity -= 1
            item.save()
            add_item_here(item.id, request.session.get('username'))
            return render(request, 'store/cart.html', {"no_stock": "FALSE", "item": item.name, "logged_in": request.session.get('is_logged_in')})
    else:
        return render(request, 'log/login.html', {"logged_in": "False"})
