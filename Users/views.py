from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from Users.forms import UserRegisterForm
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
            msg_register = "Error en los datos ingresados"
            msg_register += f" | {form.errors}"
    
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


