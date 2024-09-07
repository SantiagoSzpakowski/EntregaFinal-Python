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

class ProyectoListView(ListView):
    queryset = Proyecto.objects.all()
    context_object_name = "proyectos"
    template_name = "appprincipal/proyectos.html"

class ProyectoSeleccionadoDetailView(DetailView):
    model = Proyecto
    template_name = 'appprincipal/page.html'
    context_object_name = 'proyecto'
    pk_url_kwarg = 'id'

class ProyectoCreateView(LoginRequiredMixin, CreateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = "appprincipal/crearProyecto.html"

    def form_valid(self, form):
        form.instance.autor = self.request.user
        response = super().form_valid(form)
        # Guardar el ID del proyecto en la sesión
        self.request.session['proyecto_id'] = self.object.id
        return redirect(reverse_lazy('subirImagen', kwargs={'id': self.object.id}))
    
    def get_success_url(self):
        return reverse_lazy('subirImagen', kwargs={'id': self.object.id})


class ProyectoUpdateView(LoginRequiredMixin, UpdateView):
    model = Proyecto
    fields = ['titulo', 'subtitulo', 'fecha', 'descripcion']
    template_name = 'appprincipal/modificarProyecto.html'
    context_object_name = 'proyecto'
    pk_url_kwarg = 'id'
    
    def get_success_url(self):
        id = self.object.id
        return reverse_lazy('detalleProyecto', kwargs={'id': id})

class ProyectoDeleteView(LoginRequiredMixin, DeleteView):
    model = Proyecto
    success_url = reverse_lazy('proyectos')
    template_name = 'appprincipal/borrar_proyecto.html'

class ImagenProyectoCreateView(View):
    def get(self, request, *args, **kwargs):
        proyecto_id = self.kwargs.get('id')
        if not proyecto_id:
            return redirect('crearProyecto')

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
    model = ImagenProyecto 
    form_class = ImagenProyectoForm 
    template_name = 'appprincipal/modificar_imagen.html'
    
    context_object_name = 'imagen'
    pk_url_kwarg = 'id'
    
    def get_object(self, queryset=None):
        imagen_id = self.kwargs.get('id')  
        imagen = get_object_or_404(ImagenProyecto, id=imagen_id) 
        return imagen

    def form_valid(self, form):
        # Guarda el objeto y el archivo asociado (si se actualiza)
        form.save(commit=False)
        response = super().form_valid(form)
        return response

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form, proyecto_id=self.kwargs.get('proyecto_id')))

class ImagenDeleteView(LoginRequiredMixin, DeleteView):
    model = ImagenProyecto
    success_url = reverse_lazy('proyectos')
    template_name = 'appprincipal/borrar_imagen.html'