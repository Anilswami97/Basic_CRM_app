from django.shortcuts import render, redirect
from Authentication.forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def signin_user(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created.")
            return redirect("/")

        else:
            print(form.errors)

    else:
        form = SigninForm()
    
    context = {'form':form}
    return render(request, "Authentication/signup.html", context)



def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            authenticated_user = authenticate(username = username, password = password)
            if not authenticated_user or not authenticated_user.is_active:
                messages.danger(request, "It seems like you are not registered!")
                return redirect("/")
            else:
                login(request, authenticated_user)
                messages.success(request, "Logged in.")
                return redirect("/")
    else:
        form = LoginForm()
    context = {'form':form}

    return render(request, "Authentication/login.html", context)
            


def logout_user(request):
    logout(request)
    messages.info(request, "Logged out.")
    return redirect("/")
