from django.shortcuts import render
from django.db import connections

def store(request):
    with connections['default'].cursor() as cursor:
        cursor.execute("SELECT id, name, description, price, inventory FROM products")
        rows = cursor.fetchall()
    context = {
        'rows': rows,
    }
    return render(request, 'store/index.html', context)

def item(request, item_id): 
    with connections['default'].cursor() as cursor:
        cursor.execute("SELECT id, name, description, price, inventory FROM products")
        rows = cursor.fetchall()
    for row in rows: 
        if row[0] == item_id: 
            return render(request, 'store/item.html', {'row' : row})
   