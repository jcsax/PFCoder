from django.urls import path
from blog.views import List_posts, Create_post, Delete_post, Update_post, search_note, Detail_post, entertainment_post, economy_post, sports_post, health_post

# Nuevas URL:

urlpatterns =[
    path('', List_posts.as_view(), name = 'list_posts'),
    path('Crear-Nota/', Create_post.as_view(), name = 'create_post'),
    path('Borrar-Noticia/<int:pk>/', Delete_post.as_view(), name = 'delete_post'),
    path('Editar-Noticia/<int:pk>/', Update_post.as_view(), name = 'update_post'),
    path('Leer-Noticia/<int:pk>/', Detail_post.as_view(), name = 'detail_post'),
    path('Buscar/', search_note, name = 'search_note'),
    path('Entretenimiento/', entertainment_post, name = 'entertainment_post'),
    path('Economia/', economy_post, name = 'economy_post'),
    path('Deportes/', sports_post, name = 'sports_post'),
    path('Salud/', health_post, name = 'health_post'),
]
