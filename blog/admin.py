from django.contrib import admin
<<<<<<< HEAD
from blog.models import Economia, Entretenimiento, Salud
# Register your models here.

admin.site.register(Entretenimiento)
admin.site.register(Economia)
=======
from blog.models import Entretenimiento
from blog.models import Salud
# Register your models here.

admin.site.register(Entretenimiento)
>>>>>>> f1745d70431f24db16ad062a74d283400012f867
admin.site.register(Salud)