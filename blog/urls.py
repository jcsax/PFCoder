from django.urls import path
<<<<<<< HEAD
from blog.views import create_publi_salud, publicar_economia, publicar_entretenimiento, publicar_salud, create_publi_salud
=======
from blog.views import publicar_entretenimiento, publicar_salud
>>>>>>> f1745d70431f24db16ad062a74d283400012f867




urlpatterns = [
<<<<<<< HEAD
    path('Entretenimiento/', publicar_entretenimiento, name = 'publi_entretenimiento'),
    path('Economia/', publicar_economia, name = 'publi_economia'),
    path('Salud/', publicar_salud, name = 'publi_salud'),
    path('create-publi-salud/', create_publi_salud, name = 'create-publi-salud')
=======
    path('', publicar_entretenimiento, name = 'publi_entretenimiento'),
    path('',publicar_salud, name = 'publi_noticias_salud' )
>>>>>>> f1745d70431f24db16ad062a74d283400012f867
]