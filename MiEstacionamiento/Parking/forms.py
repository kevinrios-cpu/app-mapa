from django import forms
from .models import Usuario

class UserForm(forms.ModelForm):
    class Meta:
        model = Usuario
        widgets = {
        'password': forms.PasswordInput(),
    }