from django.db import models
from django.contrib.auth.models import User

#Perfil de Usuario
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    description = models.TextField(max_length=400, blank=True)
    city= models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to ='profile_image', default='icono_proyecto.png')
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
    def __str__(self):
        return f'Perfil de {self.user.username}'



#Contacto:
query_set = [
    [0, "Consulta"],
    [1, "Reclamo"],
    [2, "Sugerencia"]
]
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    query = models.IntegerField(choices=query_set)
    text = models.TextField(max_length=400)
    follow = models.BooleanField()
    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'

    def __str__(self):
        return self.name
