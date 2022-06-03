from django.urls import path
from blog.views import publicar_entretenimiento, publicar_salud




urlpatterns = [
    path('', publicar_entretenimiento, name = 'publi_entretenimiento'),
    path('',publicar_salud, name = 'publi_noticias_salud' )
]