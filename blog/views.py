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
    else:
        form = Salud_form(request.POST)
        if form.is_valid():
            new_publi_salud = Salud.objects.create(
                title = form.cleaned_data['title'],
                author = form.cleaned_data['author'],
                publish_date = form.cleaned_data['publish_date'],
                text = form.cleaned_data['text'],
                pic = form.cleaned_data['pic'],
            )
            context ={'new_publi_salud':new_publi_salud}
        return render(request, 'create_publi_salud.html', context=context)

def create_publi_economia(request):
    if request.method == 'GET':
        form = Economia_form()
        context = {'form':form}
        return render(request, 'create_publi_economia.html', context=context)
    else:
        form = Economia_form(request.POST)
        if form.is_valid():
            new_publi_economia = Economia.objects.create(
                title = form.cleaned_data['title'],
                author = form.cleaned_data['author'],
                publish_date = form.cleaned_data['publish_date'],
                text = form.cleaned_data['text'],
                pic = form.cleaned_data['pic'],
            )
            context ={'new_publi_economia':new_publi_economia}
        return render(request, 'create_publi_economia.html', context=context)

def create_publi_entretenimiento(request):
    if request.method == 'GET':
        form = Entretenimiento_form()
        context = {'form':form}
        return render(request, 'create_publi_entretenimiento.html', context=context)
    else:
        form = Entretenimiento_form(request.POST)
        if form.is_valid():
            new_publi_entretenimiento = Entretenimiento.objects.create(
                title = form.cleaned_data['title'],
                author = form.cleaned_data['author'],
                publish_date = form.cleaned_data['publish_date'],
                text = form.cleaned_data['text'],
                pic = form.cleaned_data['pic'],
            )
            context ={'new_publi_entretenimiento':new_publi_entretenimiento}
        return render(request, 'create_publi_entretenimiento.html', context=context)

def Buscar_Noticias_views(request):
    print(request.GET)
    Entretenimiento_buscar = Entretenimiento.objects.filter(title__icontains = request.GET['search'])
    Salud_buscar = Salud.objects.filter(title__icontains = request.GET['search'])
    Economia_buscar = Economia.objects.filter(title__icontains = request.GET['search'])
    context = {'Entretenimiento_buscar': Entretenimiento, 'Salud_buscar': Salud, 'Economia_buscar': Economia}
    return render(request, 'buscar_noticias.html', context = context)




