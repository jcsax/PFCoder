from django import forms
from blog.models import Health, Entertainment, Economy, Sports

class Health_form(forms.ModelForm):
    class Meta:
        model = Health
        fields = '__all__'

class Economy_form(forms.ModelForm):
    class Meta:
        model = Economy
        fields = '__all__'

class Entertainment_form(forms.ModelForm):
    class Meta:
        model = Entertainment
        fields = '__all__'

class Sports_form(forms.ModelForm):
    class Meta:
        model = Sports
        fields = '__all__'
