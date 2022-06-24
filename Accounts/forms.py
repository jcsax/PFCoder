from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from Accounts.models import Contact, Profile
from django.contrib.auth import get_user_model
User = get_user_model()

#Creación de usuario:
class User_registration_form(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita su contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:'' for k in fields}

#Formulario de Contacto:
class Contact_form(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

#Formulario para actualizar perfil:
class Update_profile_form(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'