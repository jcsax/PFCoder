from django.contrib import admin
from users.models import User_profile
from django.contrib.auth.models import Permission

# Register your models here.
admin.site.register(User_profile)
admin.site.register(Permission)