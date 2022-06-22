from xmlrpc.client import Boolean
from django.db.models import CharField, ImageField
from django.db import models
from django.forms import BooleanField
from django.utils.timezone import now
# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    subtitle = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    publish_date = models.DateField(default=now)
    text = models.TextField(blank=True)
    category = models.ForeignKey('Categoria', on_delete=models.CASCADE, related_name='blog')
    image = models.ImageField(upload_to='note_image', blank = True, null = True)


    class Meta:
        verbose_name = 'Nota'
        verbose_name_plural = 'Notas'
    def __str__(self):
        return self.name

class Categoria(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
    def __str__(self):
        return self.name
