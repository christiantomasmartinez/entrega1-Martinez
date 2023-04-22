from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.mi_vista, name='inicio'),
    path('registrar-comprador/', views.registrar_comprador, name='registrar_comprador'),
    path('registrar-vendedor/', views.registrar_vendedor, name='registrar_vendedor'),
    path('registrar-vehiculo/', views.registrar_vehiculo, name='registrar_vehiculo'),
    path('lista-vehiculo/', views.lista_vehiculos, name='lista_vehiculos'),
    path('registro-exitoso/', views.registro_exitoso, name='registro_exitoso'),
 ]
