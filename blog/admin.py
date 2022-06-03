from django.contrib import admin
from blog.models import Economia, Entretenimiento, Salud
# Register your models here.

admin.site.register(Entretenimiento)
admin.site.register(Economia)
admin.site.register(Salud)