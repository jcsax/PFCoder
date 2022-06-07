from django.urls import path
from blog.views import post_economy, post_entertainment, post_health, create_post_health, create_post_entertainment, create_post_economy, search_note

urlpatterns = [
    path('Entretenimiento/', post_entertainment, name = 'post_entertainment'),
    path('Economia/', post_economy, name = 'post_economy'),
    path('Salud/', post_health, name = 'post_heatlh'),
    path('Crear-Nota-Salud/', create_post_health, name = 'new_post_health'),
    path('Crear-Nota-Entretenimiento/', create_post_entertainment, name = 'new_post_entertainment'),
    path('Crear-Nota-Economia/', create_post_economy, name = 'new_post_economy'),
    path('Buscar/', search_note, name = 'search_note'),
    ]