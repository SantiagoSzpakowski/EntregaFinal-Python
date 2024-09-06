from AppPrincipal import views
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio),
    path('inicio/', views.inicio, name='inicio'), 
    path('sobremi/', views.sobremi, name='sobremi'),  
    path('proyectos/', views.ProyectoListView.as_view(), name='proyectos'),
    path('page/<int:id>/', views.ProyectoSeleccionadoDetailView.as_view(), name='detalleProyecto'), 
    path('nuevo_proyecto/', views.ProyectoCreateView.as_view(), name='crearProyecto'),
    path('subir_imagen/<int:id>/', views.ImagenProyectoCreateView.as_view(), name='subirImagen'), 
    path('modificar_imagen/<int:id>/<int:proyecto_id>', views.ImagenProyectoUpdateView.as_view(), name='modificarImagen'), 
    path('modificar_proyecto/<int:id>/', views.ProyectoUpdateView.as_view(), name='modificarProyecto'), 
    path('borrar_proyecto/<int:pk>/', views.ProyectoDeleteView.as_view(), name='borrarProyecto'), 
    path('borrar_imagen/<int:pk>/<int:proyecto_id>', views.ImagenDeleteView.as_view(), name='borrarImagen'), 

    path('usuarios/', include('Users.urls')),    
]