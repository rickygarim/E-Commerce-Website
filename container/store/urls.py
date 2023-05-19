from django.contrib import admin
from django.urls import include,path
from . import views

urlpatterns = [
    path('', views.store,name="store"),
    path('item/<int:item_id>/', views.item, name='item'),
    path('item/<str:item_name>/addToCart', views.add_to_cart, name='add_to_cart'),
]