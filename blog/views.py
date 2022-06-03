from multiprocessing import context
from django.shortcuts import render
from blog.models import Entretenimiento
from blog.models import Salud
# Create your views here.
def publicar_entretenimiento(request):
    publi_entretenimiento = Entretenimiento.objects.all()
    context = {'publi_entretenimiento': publi_entretenimiento}
    return render(request, 'publi_entretenimiento.html', context=context)

def publicar_salud(request):
    publi_noticias_salud = Salud.objects.all()
    context = {'publi_noticias_salud': publi_noticias_salud}
    return render(request, 'publi_noticias_salud.html', )