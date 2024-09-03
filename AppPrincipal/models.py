from django.db import models
from Users.models import Usuario
# Create your models here.

class Proyecto (models.Model):
    titulo = models.CharField(max_length=40)
    subtitulo = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=100)
    fecha = models.DateField()
    imagen = ""
    autor = Usuario