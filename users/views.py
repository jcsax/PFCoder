from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def profile_view(request):
    return render(request, 'profile_view.html')