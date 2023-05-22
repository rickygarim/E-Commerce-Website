from django.shortcuts import render

def login(request):
    print("this is here")
    if request.user.is_authenticated:
        return render(request, 'log/login.html', {"logged_in" : "true"})
    else:
       return render(request, 'login/login.html', {"logged_in" : "false"})
   


def logout(request):
    if request.user.is_authenticated:
        return render(request, 'log/login.html', {"logged_in" : "true"})
    else:
       return render(request, 'login/login.html', {"logged_in" : "false"}) 
   
    
   