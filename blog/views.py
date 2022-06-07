from turtle import title
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Entretenimiento, Salud, Economia
from blog.forms import Economia_form, Salud_form, Entretenimiento_form
# Create your views here.
def publicar_entretenimiento(request):
    publi_entretenimiento = Entretenimiento.objects.all()
    context = {'publi_entretenimiento': publi_entretenimiento}
    return render(request, 'publi_entretenimiento.html', context=context)

def publicar_salud(request):
    publi_salud = Salud.objects.all()
    context = {'publi_salud': publi_salud}
    return render(request, 'publi_salud.html', context=context)

def publicar_economia(request):
    publi_economia = Economia.objects.all()
    context = {'publi_economia': publi_economia}
    return render(request, 'publi_economia.html', context=context)

def create_publi_salud(request):
    if request.method == 'GET':
        form = Salud_form()
        context = {'form':form}
        return render(request, 'create_publi_salud.html', context=context)
    elif request.method == 'POST':
        form = Salud_form(request.POST)
        if form.is_valid():
            new_publi_salud = Salud.objects.create(
                title = form.cleaned_data['title'],
                author = form.cleaned_data['author'],
                publish_date = form.cleaned_data['publish_date'],
                text = form.cleaned_data['text'],
            )
            context ={'new_publi_salud':new_publi_salud}
        else:
            context ={'errors': form.errors}
    return render(request, 'create_publi_salud.html', context=context)

def create_publi_economia(request):
    if request.method == 'GET':
        form = Economia_form()
        context = {'form':form}
        return render(request, 'create_publi_economia.html', context=context)
    elif request.method == 'POST':
        form = Economia_form(request.POST)
        if form.is_valid():
            new_publi_economia = Economia.objects.create(
                title = form.cleaned_data['title'],
                author = form.cleaned_data['author'],
                publish_date = form.cleaned_data['publish_date'],
                text = form.cleaned_data['text'],
            )
            context ={'new_publi_economia':new_publi_economia}
        else:
            context ={'errors': form.errors}
    return render(request, 'create_publi_economia.html', context=context)

def create_publi_entretenimiento(request):
    if request.method == 'GET':
        form = Entretenimiento_form()
        context = {'form':form}
        return render(request, 'create_publi_entretenimiento.html', context=context)
    elif request.method == 'POST':
        form = Entretenimiento_form(request.POST)
        if form.is_valid():
            new_publi_entretenimiento = Entretenimiento.objects.create(
                title = form.cleaned_data['title'],
                author = form.cleaned_data['author'],
                publish_date = form.cleaned_data['publish_date'],
                text = form.cleaned_data['text'],
            )
            context ={'new_publi_entretenimiento':new_publi_entretenimiento}
        else:
            context = {'errors': form.errors}
    return render(request, 'create_publi_entretenimiento.html', context=context)
