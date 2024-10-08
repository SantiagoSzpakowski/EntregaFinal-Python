from Users.models import Imagen
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from Users.forms import UserPasswordForm, UserRegisterForm, UserEditForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
#from users.forms import UserEditForm, UserRegisterForm
# Create your views here.


def registroUsuario(req):
    msg_register = ""
    if req.method == 'POST':
        form = UserRegisterForm(req.POST)
        if form.is_valid():
            user = form.save()
            login(req, user)
            return redirect("inicio")
        else:
            for field, errors in form.errors.items():
                msg_register += f"Error en {field}: {', '.join(errors)}\n"
    
    form = UserRegisterForm()
    return render(req,"users/registro.html" ,  {"form":form, "msg_register": msg_register})



# Create your views here.
def loginUsuario(req):
    msg_login = ""
    if req.method == 'POST':
        form = AuthenticationForm(req, data=req.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            clave = form.cleaned_data.get('password')
            user = authenticate(username= usuario, password=clave)

            if user is not None:
                login(req, user)
                return redirect("inicio")

        msg_login = "Usuario o contraseña incorrectos"

    form = AuthenticationForm()
    return render(req, "users/usuarios.html", {"form": form, "msg_login": msg_login})

@login_required  
def editar_usuario(request):

    usuario = request.user
    if request.method == 'POST':  
        form = UserEditForm(request.POST, request.FILES, instance=usuario)
        
        if form.is_valid():
            if form.cleaned_data.get('imagen'):
                # Si el usuario ya tiene una imagen asociada (existe un objeto Imagen para este usuario)
                if Imagen.objects.filter(user=usuario).exists():
                    usuario.imagen.imagen = form.cleaned_data.get('imagen')
                    usuario.imagen.save()
                else:
                    avatar = Imagen(user=usuario, imagen=form.cleaned_data.get('imagen'))
                    avatar.save()
            form.save()
            return redirect("inicio")

    else:
        form = UserEditForm(instance=usuario)

    return render(request, "users/editar_usuario.html", {"form": form, "usuario": usuario})

class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "users/editar_clave.html"
    form_class = UserPasswordForm
    success_url = reverse_lazy("editarUsuario")