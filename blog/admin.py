from django.contrib import admin
from blog.models import Economy, Entertainment, Health
# Register your models here.

admin.site.register(Entertainment)
admin.site.register(Economy)
admin.site.register(Health)
