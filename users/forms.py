from django import forms
from Accounts.models import Profile

# #Formulario para actualizar perfil:
# class Update_profile_form(forms.ModelForm):
#     name = forms.CharField(label ='Nombre')
#     last_name = forms.CharField(label = 'Apellido')
#     description = forms.CharField(label = 'Acerca de mí')
#     city = forms.CharField(label = 'Ciudad')
#     image = forms.ImageField(label = 'Foto de perfil')
#     class Meta:
#         model = Profile
#         fields = ['name', 'last_name', 'description', 'city', 'image']