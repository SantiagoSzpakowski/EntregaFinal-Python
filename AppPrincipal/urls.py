from AppPrincipal import views
from django.urls import path

urlpatterns = [
    path('', views.inicio),
    path('inicio/', views.inicio, name='inicio'), 
    path('productos/', views.productos, name='productos'),  
    path('sobremi/', views.sobremi, name='sobremi'),  
]