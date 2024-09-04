from AppPrincipal import views
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio),
    path('inicio/', views.inicio, name='inicio'), 
    path('sobremi/', views.sobremi, name='sobremi'),  
    path('proyectos/', views.ProyectoListView.as_view(), name='proyectos'),
    path('nuevo_proyecto/', views.ProyectoCreateView.as_view(), name='crearProyecto'), 
    path('usuarios/', include('Users.urls')),    
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)