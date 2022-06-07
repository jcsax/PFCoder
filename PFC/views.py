from datetime import datetime
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Salud, Entretenimiento, Economia

def index(request):
    return render(request, 'index.html')

def registro(request):
    return render(request, 'registro.html')
    
def login(request):
    return render(request, 'login.html')

def about_us(request):
    return render(request, 'about_us.html')