from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

Usuario = get_user_model()  # Importa el modelo de usuario

# Create your models here.

class Proyecto (models.Model):
    titulo = models.CharField(max_length=40)
    subtitulo = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=2000)
    fecha = models.DateField()
    imagen = models.ForeignKey('ImagenProyecto', on_delete=models.SET_NULL, null=True, blank=True, related_name='proyectos')
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def delete(self, *args, **kwargs):
        if self.imagen:
            self.imagen.delete()
        super().delete(*args, **kwargs)
        
    def __str__(self):
        return f"{self.titulo} - {self.autor}"

class ImagenProyecto(models.Model):
    imagen = models.ImageField(upload_to='imagen', null=True, blank=True)
    
    def delete(self, *args, **kwargs):
        Proyecto.objects.filter(imagen=self).update(imagen=None)
        self.imagen.delete(save=False)
        super().delete(*args, **kwargs)

    def get_absolute_url(self):
        # Redirige a una vista que deseas mostrar después de la eliminación
        return reverse('proyectos')  # Cambia 'some_view_name' por el nombre de la vista deseada

    def __str__(self):
        return f"{self.imagen.name}"
