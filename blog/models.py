from django.db import models

# Create your models here.

class Entretenimiento(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    publish_date = models.DateField()