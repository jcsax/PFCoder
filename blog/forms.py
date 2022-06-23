from django import forms
from blog.models import Note

#Formulario para crear notas:
class Note_form(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'
