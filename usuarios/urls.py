from django.urls import path
from django.contrib.auth.views import LogoutView
from django.conf import settings
from usuarios import views

app_name = 'usuarios'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('registro/', views.registro, name='registro'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('perfil/editar/cambiar_contrasenia', views.CambiarContrasenia.as_view(), name='cambiar_contrasenia'),
    path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
    path('perfil/<str:username>/', views.perfil_usuario, name='perfil'),
    path('perfil/<str:username>/editar_descripcion/', views.editar_descripcion, name='editar_descripcion'),
    path('perfil/<str:username>/editar_enlace/', views.editar_enlace, name='editar_enlace'),
]
