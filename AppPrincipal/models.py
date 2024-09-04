from django.db import models
from django.contrib.auth import get_user_model

Usuario = get_user_model()  # Importa el modelo de usuario

# Create your models here.

class Proyecto (models.Model):
    titulo = models.CharField(max_length=40)
    subtitulo = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=500)
    fecha = models.DateField()
    imagen = models.ForeignKey('ImagenProyecto', on_delete=models.SET_NULL, null=True, blank=True, related_name='proyectos')
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.titulo} - {self.autor}"

class ImagenProyecto(models.Model):
    imagen = models.ImageField(upload_to='imagen', null=True, blank=True)
    def __str__(self):
        return f"{self.imagen.name}"
