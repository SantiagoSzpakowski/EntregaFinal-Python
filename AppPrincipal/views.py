from django.shortcuts import render

# Create your views here.

def inicio(req):
    return render(req,'appprincipal/index.html')

def proyectos(req):
    return render(req,'appprincipal/proyectos.html')

def sobremi(req):
    return render(req,'appprincipal/sobremi.html')

def usuarios(req):
    return render(req,'appprincipal/usuarios.html')

def registroUsuario(req):
    
    return render(req,'appprincipal/registro.html')