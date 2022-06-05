from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def registro(request):
    return render(request, 'registro.html')
    
def login(request):
    return render(request, 'login.html')

def about_us(request):
    return render(request, 'about_us.html')