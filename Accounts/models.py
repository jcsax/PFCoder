from os import name
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Users(AbstractBaseUser):
    user = models.CharField
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
    def __str__(self):
        return self.name


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

    def __str__(self):
        return self.name