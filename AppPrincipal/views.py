from django.shortcuts import render

# Create your views here.

def inicio(req):
    return render(req,'appprincipal/index.html')

def productos(req):
    return render(req,'appprincipal/productos.html')

def sobremi(req):
    return render(req,'appprincipal/sobremi.html')