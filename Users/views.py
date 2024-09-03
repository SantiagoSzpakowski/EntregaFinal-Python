from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from Users.forms import UserRegisterForm
#from users.forms import UserEditForm, UserRegisterForm
# Create your views here.


def usuarios(req):
    return render(req,'users/usuarios.html')

def registroUsuario(req):
    msg_register = ""
    if req.method == 'POST':
        form = UserRegisterForm(req.POST)
        print(f"Request method: {form}")
        if form.is_valid():
            user = form.save()
            login(req, user)
            return redirect("inicio")
        else:
            msg_register = "Error en los datos ingresados"
            msg_register += f" | {form.errors}"
    
    form = UserRegisterForm()
    return render(req,"users/registro.html" ,  {"form":form})



# Create your views here.
def login_request(request):
    msg_login = ""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return render(request, "AppCoder/index.html")

        msg_login = "Usuario o contraseña incorrectos"

    form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form, "msg_login": msg_login})

# Vista de registro
#def register(request):
    msg_register = ""
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Si los datos ingresados en el form son válidos, con form.save()
            # creamos un nuevo user usando esos datos
            form.save()
            return render(request,"AppCoder/index.html")
        else:
            msg_register = "Error en los datos ingresados"
            msg_register += f" | {form.errors}"

    form = UserRegisterForm()     
    return render(request,"users/registro.html" ,  {"form":form, "msg_register": msg_register})
