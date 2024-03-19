from django.shortcuts import render, redirect
from Home.forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "Home/home.html")