from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from AppPrincipal.models import ImagenProyecto, Proyecto
from AppPrincipal.forms import ProyectoForm, ImagenProyectoForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render

class ProyectoListView(ListView):
    queryset = Proyecto.objects.all()  # Definiendo el QuerySet directamente
    #model: Proyecto #Esto lo agrego despues de hacer el create modif y delete, al agregar esto borro el de arriba
    context_object_name = "proyectos"
    template_name = "appprincipal/proyectos.html"

class ProyectoSeleccionadoListView(ListView):
    model = Proyecto
    template_name = 'appprincipal/page.html'  # Asegúrate de que esta ruta sea correcta
    context_object_name = 'proyecto'  # El nombre del contexto que se pasa a la plantilla

    def get_queryset(self):
        proyecto_id = self.kwargs['id']
        return Proyecto.objects.filter(id=proyecto_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Puedes agregar más datos al contexto si es necesario
        # Por ejemplo, obtener el proyecto específico
        proyecto_id = self.kwargs['id']
        context['proyecto'] = Proyecto.objects.get(id=proyecto_id)
        return context
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

class ImagenProyectoCreateView(View):
    def get(self, request, *args, **kwargs):
        proyecto_id = request.session.get('proyecto_id')
        if not proyecto_id:
            return redirect('crearProyecto')  # Redirige si no hay proyecto

        proyecto = get_object_or_404(Proyecto, id=proyecto_id)
        imagen_form = ImagenProyectoForm()
        return render(request, 'appprincipal/subir_imagen.html', {'imagen_form': imagen_form})

    def post(self, request, *args, **kwargs):
        proyecto_id = request.session.get('proyecto_id')
        if not proyecto_id:
            return redirect('crearProyecto')  # Redirige si no hay proyecto

        proyecto = get_object_or_404(Proyecto, id=proyecto_id)
        imagen_form = ImagenProyectoForm(request.POST, request.FILES)
        
        if request.FILES.get('imagen'):
            if imagen_form.is_valid():
                imagen_proyecto = imagen_form.save()
                proyecto.imagen = imagen_proyecto
                proyecto.save()
                return redirect('proyectos')  # Redirige a la lista de proyectos después de guardar

        return render(request, 'appprincipal/subir_imagen.html', {'imagen_form': imagen_form})
    





# Create your views here.

def inicio(req):
    return render(req,'appprincipal/index.html')

def sobremi(req):
    return render(req,'appprincipal/sobremi.html')

def detalleProyecto(req):
    return render(req,'appprincipal/page.html')
