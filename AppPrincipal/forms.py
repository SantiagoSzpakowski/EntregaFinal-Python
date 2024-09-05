from django import forms
from AppPrincipal.models import Proyecto,ImagenProyecto

class ProyectoForm(forms.ModelForm):
    titulo = forms.CharField(
        label="Titulo",
        widget=forms.TextInput(attrs={'placeholder': 'Titulo', 'class': 'form-control'}))
    subtitulo = forms.CharField(
        label="Subtitulo",
        widget=forms.TextInput(attrs={'placeholder': 'Subtitulo', 'class': 'form-control'}))
    fecha = forms.DateField(
        label="Fecha",
        widget=forms.DateInput(attrs={'placeholder': 'Fecha', 'class': 'form-control', 'type': 'date'}))
    imagen = forms.ImageField(
        label="Imagen", 
        required=False, 
        widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'type': 'file'}))
    class Meta:
        model = Proyecto
        fields = ['id','titulo', 'subtitulo', 'fecha','imagen', 'descripcion']
        widgets = {
            'descripcion': forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Descripción',
            'style': 'height: 10rem;'
            }),
        }   
        
        
class ImagenProyectoForm(forms.ModelForm):
    class Meta:
        model = ImagenProyecto
        fields = ['imagen']
        widgets = {
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control', 'type': 'file'})
        }