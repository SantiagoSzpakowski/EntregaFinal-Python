from django.db import models
from Users.models import Usuario

# Create your models here.

class Proyecto (models.Model):
    titulo = models.CharField(max_length=40)
    subtitulo = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=100)
    fecha = models.DateField()
    imagen = models.ForeignKey('ImagenProyecto', on_delete=models.SET_NULL, null=True, blank=True, related_name='proyectos')
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class ImagenProyecto(models.Model):
    imagen = models.ImageField(upload_to='imagen', null=True, blank=True)
    def __str__(self):
        return f"{self.imagen}"
