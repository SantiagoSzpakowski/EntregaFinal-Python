from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
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


class UserEditForm(UserChangeForm):
    password = None

    first_name = forms.CharField(
        label="Nombre",
        widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Mail', 'class': 'form-control'}))
    imagen = forms.ImageField(label="Avatar", required=False)
    
    class Meta:
        model = User                
        fields = ['first_name','email', 'imagen']  

class UserPasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Contraseña Actual",
        widget=forms.PasswordInput(attrs={'placeholder': 'Introduce tu contraseña actual', 'class': 'form-control'})
    )
    new_password1 = forms.CharField(
        label="Nueva Contraseña",
        widget=forms.PasswordInput(attrs={'placeholder': 'Introduce tu nueva contraseña', 'class': 'form-control'})
    )
    new_password2 = forms.CharField(
        label="Confirmar Nueva Contraseña",
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirma tu nueva contraseña', 'class': 'form-control'})
    )