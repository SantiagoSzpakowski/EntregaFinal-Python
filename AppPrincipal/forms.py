from django import forms
from AppPrincipal.models import Proyecto

class ProyectoForm(forms.ModelForm):
    imagen = forms.ImageField(
        label="Imagen", 
        required=False, 
        widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'type': 'file'}))
    titulo = forms.CharField(
        label="Titulo",
        widget=forms.TextInput(attrs={'placeholder': 'Titulo', 'class': 'form-control'}))
    subtitulo = forms.CharField(
        label="Subtitulo",
        widget=forms.TextInput(attrs={'placeholder': 'Subtitulo', 'class': 'form-control'}))
    fecha = forms.DateField(
        label="Fecha",
        widget=forms.DateInput(attrs={'placeholder': 'Fecha', 'class': 'form-control', 'type': 'date'}))
    class Meta:
        model = Proyecto
        fields = ['imagen','titulo', 'subtitulo', 'descripcion', 'fecha']
        widgets = {
            'descripcion': forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Descripción',
            'style': 'height: 10rem;'
            }),
        }   