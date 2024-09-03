from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from AppPrincipal.models import Proyecto

class ProyectoListView(ListView):
    queryset = Proyecto.objects.all()  # Definiendo el QuerySet directamente
    #model: Proyecto --Esto lo agrego despues de hacer el create modif y delete, al agregar esto borro el de arriba
    context_object_name = "proyectos"
    template_name = "appprincipal/proyectos.html"













from django.shortcuts import render

# Create your views here.

def inicio(req):
    return render(req,'appprincipal/index.html')

#def proyectos(req):
#    return render(req,'appprincipal/proyectos.html')

def sobremi(req):
    return render(req,'appprincipal/sobremi.html')

def usuarios(req):
    return render(req,'appprincipal/usuarios.html')

def registroUsuario(req):
    return render(req,'appprincipal/registro.html')