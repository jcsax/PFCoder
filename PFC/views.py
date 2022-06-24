from django.shortcuts import render
from blog.models import Note


#Inicio:
def index(request):
    inicio = Note.objects.all().order_by('-publish_date')[:4]
    return render(request, 'index.html', {'inicio': inicio})
#Acerca de Nosotros:
def about_us(request):
    return render(request, 'about_us.html')
