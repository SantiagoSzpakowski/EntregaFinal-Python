from AppPrincipal import views
from django.urls import path

urlpatterns = [
    path('', views.inicio),
    path('inicio/', views.inicio, name='inicio'), 
    path('sobremi/', views.sobremi, name='sobremi'),  
    path('productos/', views.productos, name='productos'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('registro/', views.registroUsuario, name='registro'),    
]