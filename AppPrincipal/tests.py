from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from AppPrincipal.models import Proyecto
from django.core import mail
from django.utils import timezone
from django.test import Client
from Users.forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm

class RegistroUsuarioTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('registro')

    def test_registro_usuario_valido(self):
        form_data = {
            'username': 'usuario_prueba',
            'first_name': 'usuario_nombre',
            'password1': 'contraseña_segura',
            'password2': 'contraseña_segura',
            'email': 'usuario_prueba@example.com'
        }
        
        response = self.client.post(self.url, data=form_data)
        
        # Verifica que el usuario haya sido creado
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'usuario_prueba')

        # Verifica que el usuario haya sido autenticado y redirigido
        self.assertRedirects(response, reverse('inicio'))
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_registro_usuario_formulario_invalido(self):
        form_data = {
            'username': 'usuario_prueba',
            'first_name': 'usuario_nombre',
            'password1': 'contraseña_segura',
            'password2': 'diferente_contraseña',  # Contraseña no coincide
            'email': 'usuario_prueba@example.com'
        }
        
        response = self.client.post(self.url, data=form_data)
        
        # Verifica que no se haya creado un usuario
        self.assertEqual(User.objects.count(), 0)
        
        # Verifica que la página se haya renderizado de nuevo con errores
        self.assertTemplateUsed(response, 'users/registro.html')
        self.assertContains(response, 'Error en password2')

    def test_registro_usuario_metodo_get(self):
        response = self.client.get(self.url)
        
        # Verifica que la página de registro se renderiza
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/registro.html')
        self.assertIsInstance(response.context['form'], UserRegisterForm)
        self.assertEqual(response.context['msg_register'], "")


class LoginUsuarioTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Crear un usuario de prueba para autenticar
        cls.usuario = User.objects.create_user(username='usuario_prueba', password='contraseña_prueba')

    def test_login_usuario_exitoso(self):
        # Simular un inicio de sesión exitoso
        form_data = {
            'username': 'usuario_prueba',
            'password': 'contraseña_prueba'
        }
        response = self.client.post(reverse('usuarios'), data=form_data)
        
        # Verificar que el login fue exitoso y se redirige correctamente
        self.assertEqual(response.status_code, 302) 
        self.assertRedirects(response, reverse('inicio'))

    def test_login_usuario_incorrecto(self):
        # Simular un inicio de sesión con credenciales incorrectas
        form_data = {
            'username': 'usuario_prueba',
            'password': 'contraseña_incorrecta'
        }
        response = self.client.post(reverse('usuarios'), data=form_data)
        
        # Verificar que la página de login se vuelve a cargar y muestra el mensaje de error
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Usuario o contraseña incorrectos")

    def test_login_get_request(self):
        # Simular una solicitud GET a la vista de login
        response = self.client.get(reverse('usuarios'))

        # Verificar que la página de login se carga correctamente
        self.assertEqual(response.status_code, 200)


class ProyectoCreateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.usuario = User.objects.create_user(username='usuario_prueba', password='contraseña_prueba')

    def setUp(self):
        self.client.login(username='usuario_prueba', password='contraseña_prueba')

    def test_create_proyecto(self):
        # Simula la creación de un proyecto
        form_data = {
            'titulo': 'Nuevo Proyecto',
            'subtitulo': 'Subtitulo',
            'descripcion': 'Descripción',
            'fecha': timezone.now().date()
        }
        response = self.client.post(reverse('crearProyecto'), data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Proyecto.objects.count(), 1)
        nuevo_proyecto = Proyecto.objects.first()
        self.assertEqual(nuevo_proyecto.titulo, 'Nuevo Proyecto')
        self.assertEqual(nuevo_proyecto.autor, self.usuario)
        self.assertIsInstance(response.context['form'], AuthenticationForm)