from Users import views
from django.urls import path
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('usuarios/', views.loginUsuario, name='usuarios'),
    path('registro/', views.registroUsuario, name='registro'),
    path('logout/', LogoutView.as_view(next_page='inicio'), name="logout"),

]