# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser

# class User_profile(AbstractBaseUser):
#     user = models.CharField('Nombre de usuario', unique = True, max_length=50)
#     email = models.EmailField('Correo Electronico', max_length=120, unique=True, blank = False, null = True)
#     phone = models.CharField(max_length=20)
#     name = models.CharField('Nombres', max_length=120, blank=True, null=True)
#     last_name = models.CharField('Apellido', max_length=120, blank=True, null=True)
#     city = models.CharField(max_length=40, blank = True)
#     profile_image = models.ImageField('Imagen de Perfil', upload_to='profile_image')
#     user_is_active = models.BooleanField(default = True)
#     user_admin = models.BooleanField(default = False)

#     USERNAME_FIELD = 'user'
#     REQUIRED_FIELDS = ['email', 'name', 'last_name']
#     class Meta:
#         verbose_name = 'Perfil de Usuario'
#         verbose_name_plural = 'Perfiles de Usuarios'
#     def __str__(self):
#         return f'User_profile{self.name}'