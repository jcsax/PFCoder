from django.urls import path
from blog.views import List_posts, Create_post, Delete_post, Update_post, search_note, Detail_post, entertainment_post, economy_post, sports_post, health_post

# Nuevas URL:

urlpatterns =[
    path('', List_posts.as_view(), name = 'list_posts'),
    path('crear-nota/', Create_post.as_view(), name = 'create_post'),
    path('borrar-noticia/<int:pk>/', Delete_post.as_view(), name = 'delete_post'),
    path('editar-noticia/<int:pk>/', Update_post.as_view(), name = 'update_post'),
    path('leer-noticia/<int:pk>/', Detail_post.as_view(), name = 'detail_post'),
    path('buscar/', search_note, name = 'search_note'),
    path('entretenimiento/', entertainment_post, name = 'entertainment_post'),
    path('economia/', economy_post, name = 'economy_post'),
    path('deportes/', sports_post, name = 'sports_post'),
    path('salud/', health_post, name = 'health_post'),
]
