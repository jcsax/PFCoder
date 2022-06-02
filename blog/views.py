from django.shortcuts import render
from blog.models import Entretenimiento
# Create your views here.
def publicar_entretenimiento(request):
    publi_entretenimiento = Entretenimiento.objects.all()
    context = {'publi_entretenimiento': publi_entretenimiento}
    return render(request, 'publi_entretenimiento.html', context=context)