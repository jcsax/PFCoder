from datetime import datetime
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect
from blog.models import Note


#Inicio:
def index(request):
    inicio = Note.objects.all().order_by('publish_date')[6:10]
    return render(request, 'index.html', {'inicio': inicio})
#Todas las Noticias:
def bd(request):
    bd_view = Note.objects.all()
    context = {'bd_view': bd_view}
    return render(request,'bd.html', context=context)
#Acerca de Nosotros:
def about_us(request):
    return render(request, 'about_us.html')
