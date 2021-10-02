from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import FormLogin

# Create your views here.
def form(request):
    form = FormLogin()
    
    if request.method == 'POST':
        username_login = request.POST['username']
        password_login = request.POST['password']

        user = authenticate(request, username = username_login, password = password_login)

        if user is not None:
            login(request, user)
            return redirect('/dashboard/')

    return render(request, "login/index.html", {'form' : form})