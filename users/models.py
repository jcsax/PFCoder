from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User_profile(AbstractBaseUser):
    user = models.CharField('Nombre de usuario', unique = True, max_length=50)
    email = models.EmailField('Correo Electronico', max_length=120, unique=True)
    phone = models.CharField(max_length=20)
    name = models.CharField('Nombres', max_length=120, blank=True, null=True)
    last_name = models.CharField('Apellido', max_length=120, blank=True, null=True)
    city = models.CharField(max_length=40)
    profile_image = models.ImageField('Imagen de Perfil', upload_to='profile_image')
    user_is_active = models.BooleanField(default = True)
    user_admin = models.BooleanField(default = False)

    USERNAME_FIELD = 'user'
    REQUIRED_FIELDS = ['email', 'name', 'last_name']

    def __str__(self):
        return f'User_profile{self.name}'

    def has_perm(self, perm, obj = None):
        return True
    
    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.user_admin