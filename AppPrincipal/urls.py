from AppPrincipal import views
from django.urls import path

urlpatterns = [
    path('', views.inicio),
    path('inicio/', views.inicio, name='inicio'),    
]