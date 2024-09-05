from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from AppPrincipal.models import ImagenProyecto, Proyecto
from AppPrincipal.forms import ProyectoForm, ImagenProyectoForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render


# Create your views here.

def inicio(req):
    return render(req,'appprincipal/index.html')

def sobremi(req):
    return render(req,'appprincipal/sobremi.html')

def editar(req):
    return render(req,'appprincipal/modificarProyecto.html')

class ProyectoListView(ListView):
    queryset = Proyecto.objects.all()  # Definiendo el QuerySet directamente
    #model: Proyecto #Esto lo agrego despues de hacer el create modif y delete, al agregar esto borro el de arriba
    context_object_name = "proyectos"
    template_name = "appprincipal/proyectos.html"

class ProyectoSeleccionadoDetailView(DetailView):
    model = Proyecto
    template_name = 'appprincipal/page.html'
    context_object_name = 'proyecto'
    pk_url_kwarg = 'id'

#En creacion o modificacion de Proyecto agregar en el html min 27 zoom de imagen avatar

class ProyectoCreateView(LoginRequiredMixin, CreateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = "appprincipal/crearProyecto.html"
    success_url = reverse_lazy("subirImagen")

    def form_valid(self, form):
        form.instance.autor = self.request.user
        response = super().form_valid(form)
        # Guardar el ID del proyecto en la sesión
        self.request.session['proyecto_id'] = self.object.id
        return response

class ProyectoUpdateView(LoginRequiredMixin, UpdateView):
    model = Proyecto
    fields = ['titulo', 'subtitulo', 'fecha', 'descripcion']
    template_name = 'appprincipal/modificarProyecto.html'
    context_object_name = 'proyecto'
    pk_url_kwarg = 'id'
    
    def get_success_url(self):
        id = self.object.id
        return reverse_lazy('detalleProyecto', kwargs={'id': id})


class ImagenProyectoCreateView(View):
    def get(self, request, *args, **kwargs):
        proyecto_id = self.kwargs.get('id')
        if not proyecto_id:
            return redirect('crearProyecto')  # Redirige si no hay proyecto

        proyecto = get_object_or_404(Proyecto, id=proyecto_id)
        imagen_form = ImagenProyectoForm()
        return render(request, 'appprincipal/subir_imagen.html', {'imagen_form': imagen_form})

    def post(self, request, *args, **kwargs):
        proyecto_id = self.kwargs.get('id')
        if not proyecto_id:
            return redirect('crearProyecto')

        proyecto = get_object_or_404(Proyecto, id=proyecto_id)
        imagen_form = ImagenProyectoForm(request.POST, request.FILES)
        
        if request.FILES.get('imagen'):
            if imagen_form.is_valid():
                imagen_proyecto = imagen_form.save()
                proyecto.imagen = imagen_proyecto
                proyecto.save()
                return redirect('proyectos') 

        return render(request, 'appprincipal/subir_imagen.html', {'imagen_form': imagen_form})
    


class ImagenProyectoUpdateView(UpdateView):
    model = ImagenProyecto  # El modelo que estás actualizando
    form_class = ImagenProyectoForm  # El formulario que utilizarás
    template_name = 'appprincipal/modificar_imagen.html'  # La plantilla que se usa para el formulario
    
    context_object_name = 'imagen'
    pk_url_kwarg = 'id'
    
    def get_object(self, queryset=None):
        # Obtener el id de la imagen desde la URL
        imagen_id = self.kwargs.get('id')  # 'pk' es el identificador primario de la imagen
        imagen = get_object_or_404(ImagenProyecto, id=imagen_id)  # Obtén la imagen a través de su id
        return imagen

    def form_valid(self, form):
        form.save()  # Guardamos la imagen actualizada

        # Obtener el proyecto_id que viene de la URL y devolverlo en la redirección
        proyecto_id = self.kwargs.get('proyecto_id')  # Capturamos el id del proyecto de la URL

        # Redirigir a una vista que incluya el proyecto_id (puedes ajustar la URL de redirección según tus necesidades)
        return redirect('detalleProyecto', proyecto_id)#, proyecto_id=proyecto_id)

    def form_invalid(self, form):
        # Si el formulario no es válido, volvemos a renderizar la página con el formulario
        return self.render_to_response(self.get_context_data(form=form, proyecto_id=self.kwargs.get('proyecto_id')))