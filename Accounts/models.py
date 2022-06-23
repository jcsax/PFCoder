from msilib.schema import Class
from os import name
from django.db import models


#Acá van los perfiles de usuario. Crear Model



#Formulario de contacto:
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