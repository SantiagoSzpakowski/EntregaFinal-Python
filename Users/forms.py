from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label="Usuario", 
        widget=forms.TextInput(attrs={'placeholder': 'Nombre de Usuario', 'class': 'form-control'}))
    first_name = forms.CharField(
        label="Nombre",
        widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Mail', 'class': 'form-control'}))
    password1 = forms.CharField(
        label='Contraseña', 
        widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'class': 'form-control'})
    )
    password2 = forms.CharField(
        label='Confirmar Contraseña', 
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirma tu Contraseña', 'class': 'form-control'})
    )
    class Meta:
        model = User
        fields = ["username", "first_name", "email", "password1", "password2"]
        