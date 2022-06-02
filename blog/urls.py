from django.urls import path
from blog.views import publicar_entretenimiento




urlpatterns = [
    path('', publicar_entretenimiento, name = 'publi_entretenimiento')
]