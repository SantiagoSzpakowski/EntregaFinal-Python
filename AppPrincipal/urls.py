from AppPrincipal import views
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio),
    path('inicio/', views.inicio, name='inicio'), 
    path('sobremi/', views.sobremi, name='sobremi'),  
    path('proyectos/', views.ProyectoListView.as_view(), name='proyectos'),
    path('page/<int:id>/', views.ProyectoSeleccionadoListView.as_view(), name='detalleProyecto'), 
    path('nuevo_proyecto/', views.ProyectoCreateView.as_view(), name='crearProyecto'),
    path('subir_imagen/', views.ImagenProyectoCreateView.as_view(), name='subirImagen'), 
    path('usuarios/', include('Users.urls')),    
]