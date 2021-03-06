from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Account
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            user = User.objects.create_user(username=first_name, email=email, password=password, first_name=first_name, last_name=last_name)
            user.save()
            account = Account(user=user, first_name=first_name, last_name=last_name, username=first_name, email=email, phone_number=phone)
            account.save()
            messages.success(request, 'Registration successful')
            return redirect ('register') 

    return render(request, 'register.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)

            return redirect('index')
        else:
            messages.error(request, 'invalid login credentials')
            return redirect('signin')

    return render(request, 'signin.html')

@login_required
def signout(request):
    logout(request)
    messages.success(request,"You're are logged out")
    return redirect('signin')