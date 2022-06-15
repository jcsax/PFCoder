from django.db.models import CharField, ImageField
from django.db import models
from django.utils.timezone import now
# Create your models here.

class Entertainment(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    #subtitle = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    publish_date = models.DateField(default=now)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='Entertainment_image', blank = True, null = True)

    class Meta:
        verbose_name = 'Entretenimiento'
        verbose_name_plural = 'Entretenimiento'


class Economy(models.Model):
    title = models.CharField(max_length=100)
    #subtitle = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    publish_date = models.DateField(default=now)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='Economy_image', blank = True, null = True)
    class Meta:
        verbose_name = 'Economia'
        verbose_name_plural = 'Economia'

class Health(models.Model):
    title = models.CharField(max_length=100)
    #subtitle = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    publish_date = models.DateField(default=now)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='Healt_image', blank = True, null = True)
    class Meta:
        verbose_name = 'Salud'
        verbose_name_plural = 'Salud'
