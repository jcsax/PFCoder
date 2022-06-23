from operator import concat
from pyexpat import model
from django.shortcuts import render, redirect
from multiprocessing import context
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from Accounts.forms import User_registration_form, Contact_form
from users.models import User_profile
from django.contrib.auth.mixins import LoginRequiredMixin





#Modulo Login:
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                context = {'message':f'Hola de nuevo {username}'}
                return render(request, 'logged_up.html', context = context)
            else:
                context = {'errors':'Tus datos son incorrectos!'}
                form = AuthenticationForm()
                return render(request, 'auth/login.html', context = context)
        else:
            errors = form.errors
            form = AuthenticationForm()
            context = {'errors':errors, 'form':form} 
            return render(request, 'auth/login.html', context = context)
    else:
        form = AuthenticationForm()
        context = {'form':form}
        return render(request, 'auth/login.html', context = context)

#Modulo Register:
def register_view(request):
    if request.method == 'POST':
        form = User_registration_form(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            context = {'message':f'Usuario creado correctamente, bienvenido {username}'}
            return render(request, 'new_user.html', context = context)
        else:
            errors = form.errors
            form = User_registration_form()
            context = {'errors':errors, 'form':form}
            return render(request, 'auth/register.html', context = context)
    else:
        form = User_registration_form()
        context = {'form':form}
        return render(request, 'auth/register.html', context =context)

#Logout:
def logout_view(request):
    logout(request)
    return redirect('/index')

#Contact Form:
def contact_view(request):
    data = {
        'contact_form': Contact_form()
    }
    if request.method == 'POST':
        contact_full = Contact_form(data=request.POST)
        if contact_full.is_valid():
            contact_full.save()
            data["message"] = "Contacto enviado"
        else:
            data['contact_form'] = contact_full

    return render(request, 'contact_form.html', data)

#Perfil de usuario
