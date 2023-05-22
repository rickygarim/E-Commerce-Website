from django.contrib.auth import views as auth_views
from django.urls import include,path
from . import views

urlpatterns = [
    # other URL patterns
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    
    
]