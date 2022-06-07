from datetime import datetime
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def sign_in(request):
    return render(request, 'sign-in.html')
    
def login(request):
    return render(request, 'login.html')

def about_us(request):
    return render(request, 'about_us.html')