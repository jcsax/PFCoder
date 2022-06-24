from pyexpat import model
from re import template
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse_lazy
from users.models import User_profile
from django.views import generic
from django.views.generic import UpdateView
# Create your views here.

class profile_view(generic.UpdateView):
    model = User_profile
    template_name = 'profile_view.html'
    fields = '__all__'
    success_url = reverse_lazy('perfil/')
    