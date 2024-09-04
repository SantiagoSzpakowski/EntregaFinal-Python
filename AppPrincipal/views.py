from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from AppPrincipal.models import ImagenProyecto, Proyecto
from AppPrincipal.forms import ProyectoForm
from django.contrib.auth.mixins import LoginRequiredMixin

class ProyectoListView(ListView):
    queryset = Proyecto.objects.all()  # Definiendo el QuerySet directamente
    #model: Proyecto #Esto lo agrego despues de hacer el create modif y delete, al agregar esto borro el de arriba
    context_object_name = "proyectos"
    template_name = "appprincipal/proyectos.html"


#En creacion o modificacion de Proyecto agregar en el html min 27 zoom de imagen avatar

class ProyectoCreateView(LoginRequiredMixin, CreateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = "appprincipal/crearProyecto.html"    
    
    success_url = reverse_lazy("proyectos") 
    
    def form_valid(self, form):
        # Asigna el usuario actual como autor del proyecto
        form.instance.autor = self.request.user
        print("Autor asignado:", form.instance.autor)
        
        # Guarda el proyecto sin confirmar aún
        response = super().form_valid(form)
        
        # Verifica si hay un archivo de imagen
        if 'imagen' in self.request.FILES:
            imagen_form = self.request.FILES['imagen']
            print("Archivo de imagen recibido:", imagen_form)
            if imagen_form:
                # Crea y guarda una instancia de ImagenProyecto
                imagen_proyecto = ImagenProyecto(imagen=imagen_form)
                imagen_proyecto.save()
                print("Imagen guardada:", imagen_proyecto)
                
                # Asigna la instancia de ImagenProyecto al campo imagen del proyecto
                self.object.imagen = imagen_proyecto
                self.object.save()
                print("Proyecto actualizado con imagen:", self.object)
        
        return response







from django.shortcuts import render

# Create your views here.

def inicio(req):
    return render(req,'appprincipal/index.html')

def nuevoproyecto(req):
    return render(req,'appprincipal/crearProyecto.html')

def sobremi(req):
    return render(req,'appprincipal/sobremi.html')

