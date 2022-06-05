from django.db import models

# Create your models here.

class Entretenimiento(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    author = models.CharField(max_length=50)
    publish_date = models.DateField()
    text = models.TextField(blank=True)
    pic = models.ImageField(upload_to='entretenimiento', null=True)
    class Meta:
        verbose_name = 'Entretenimiento'
        verbose_name_plural = 'Entretenimiento'


class Economia(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    publish_date = models.DateField()
    text = models.TextField(blank=True)
    pic = models.ImageField(upload_to='economia', null=True)
    class Meta:
        verbose_name = 'Economia'
        verbose_name_plural = 'Economia'

class Salud(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    publish_date = models.DateField()
    text = models.TextField(blank=True)
    pic = models.ImageField(upload_to='salud', null=True)
    class Meta:
        verbose_name = 'Salud'
        verbose_name_plural = 'Salud'

