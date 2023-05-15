from django.shortcuts import render
from django.db import connections

def index(request):
    with connections['default'].cursor() as cursor:
        cursor.execute("SELECT name, description, price, inventory FROM products")
        rows = cursor.fetchall()
    context = {
        'rows': rows,
    }
    return render(request, 'store/index.html', context)
