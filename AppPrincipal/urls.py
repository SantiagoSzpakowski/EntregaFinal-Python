from AppPrincipal import views
from django.urls import include, path

urlpatterns = [
    path('', views.inicio),
    path('inicio/', views.inicio, name='inicio'), 
    path('sobremi/', views.sobremi, name='sobremi'),  
    path('proyectos/', views.ProyectoListView.as_view(), name='proyectos'),
    #path('usuarios/', include('Users.urls'), name='usuarios'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('registro/', views.registroUsuario, name='registro'),    
]