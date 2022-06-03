from django.urls import path

from blog.views import create_publi_salud, publicar_economia, publicar_entretenimiento, publicar_salud, create_publi_salud, create_publi_entretenimiento, create_publi_economia

urlpatterns = [
    path('Entretenimiento/', publicar_entretenimiento, name = 'publi_entretenimiento'),
    path('Economia/', publicar_economia, name = 'publi_economia'),
    path('Salud/', publicar_salud, name = 'publi_salud'),
    path('create-publi-salud/', create_publi_salud, name = 'create-publi-salud'),
    path('create-publi-entretenimiento/', create_publi_entretenimiento, name = 'create-publi-entretenimiento'),
    path('create-publi-economia/', create_publi_economia, name = 'create-publi-economia'),
    ]