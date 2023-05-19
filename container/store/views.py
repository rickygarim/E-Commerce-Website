from django.shortcuts import render
from . models import Product
from django.db import connections

# def store(request):
#     with connections['default'].cursor() as cursor:
#         cursor.execute("SELECT id, name, description, price, inventory FROM products")
#         rows = cursor.fetchall()
#     context = {
#         'rows': rows,
#     }
#     return render(request, 'store/index.html', context)

# def item(request, item_id): 
#     with connections['default'].cursor() as cursor:
#         cursor.execute("SELECT id, name, description, price, inventory FROM products")
#         rows = cursor.fetchall()
#     for row in rows: 
#         if row[0] == item_id: 
#             return render(request, 'store/item.html', {'row' : row})

def store(request):
    all_products = Product.objects.all()
    context = []
    for thing in all_products: 
        if thing.quantity > 0: 
            context.append([thing.id, thing.name, thing.description, thing.price, thing.quantity, thing.colors_types, thing.images])
    return render(request, 'store/index.html', {"rows" : context})
     
    
def item(request, item_id):
    thing = Product.objects.filter(id=item_id)
    wild_books = [thing[0].id, thing[0].name, thing[0].description, thing[0].price, thing[0].quantity, thing[0].colors_types, thing[0].images]
    return render(request, 'store/item.html', {'row' :  wild_books})

    
def add_to_cart(request, item_name): 
    all_data = Product.objects.filter(id=item_name)
    item = all_data[0]

    if item.quantity <= 0: 
        return render(request, 'store/cart.html', {"no_stock" : "TRUE", item: ""})
    else: 
        item.quantity -= 1
        item.save()
        # ADD THIS ITEM TO CURRENT USERS CART 
        return render(request, 'store/cart.html', {"no_stock" : "FALSE", "item": item.name })