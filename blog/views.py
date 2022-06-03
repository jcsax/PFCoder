<<<<<<< HEAD
from turtle import title
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Entretenimiento, Salud, Economia
from blog.forms import Salud_form
=======
from multiprocessing import context
from django.shortcuts import render
from blog.models import Entretenimiento
from blog.models import Salud
>>>>>>> f1745d70431f24db16ad062a74d283400012f867
# Create your views here.
def publicar_entretenimiento(request):
    publi_entretenimiento = Entretenimiento.objects.all()
    context = {'publi_entretenimiento': publi_entretenimiento}
    return render(request, 'publi_entretenimiento.html', context=context)

def publicar_salud(request):
<<<<<<< HEAD
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





=======
    publi_noticias_salud = Salud.objects.all()
    context = {'publi_noticias_salud': publi_noticias_salud}
    return render(request, 'publi_noticias_salud.html', )
>>>>>>> f1745d70431f24db16ad062a74d283400012f867
