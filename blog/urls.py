from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from blog.views import create_post_sports, post_economy, post_entertainment, post_health, create_post_health, create_post_entertainment, create_post_economy, post_sports, search_note

urlpatterns = [
    path('Entretenimiento/', post_entertainment, name = 'post_entertainment'),
    path('Economia/', post_economy, name = 'post_economy'),
    path('Salud/', post_health, name = 'post_heatlh'),
    path('Deportes/', post_sports, name = 'post_sports'),
    path('Crear-Nota-Salud/', create_post_health, name = 'new_post_health'),
    path('Crear-Nota-Entretenimiento/', create_post_entertainment, name = 'new_post_entertainment'),
    path('Crear-Nota-Economia/', create_post_economy, name = 'new_post_economy'),
    path('Crear-Nota-Deportes/', create_post_sports, name = 'new_post_sports'),
    path('Buscar/', search_note, name = 'search_note'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)