from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from AppPrincipal.models import Proyecto

class ProyectoListView(ListView):
    queryset = Proyecto.objects.all()  # Definiendo el QuerySet directamente
    #model: Proyecto --Esto lo agrego despues de hacer el create modif y delete, al agregar esto borro el de arriba
    context_object_name = "proyectos"
    template_name = "appprincipal/proyectos.html"
    

#En creacion o modificacion de Proyecto agregar en el html min 27 zoom de imagen avatar













from django.shortcuts import render

# Create your views here.

def inicio(req):
    return render(req,'appprincipal/index.html')

#def proyectos(req):
#    return render(req,'appprincipal/proyectos.html')

def sobremi(req):
    return render(req,'appprincipal/sobremi.html')

