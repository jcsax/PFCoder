from django import forms
from blog.models import Salud, Entretenimiento, Economia

class Salud_form(forms.ModelForm):
    class Meta:
        model = Salud
        fields = '__all__'

class Economia_form(forms.ModelForm):
    class Meta:
        model = Economia
        fields = '__all__'

class Entretenimiento_form(forms.ModelForm):
    class Meta:
        model = Entretenimiento
        fields = '__all__'

