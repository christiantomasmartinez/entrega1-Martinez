from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.mi_vista, name='inicio'),
    path('about/', views.about, name='about'),
    path('registrar-vehiculo/', views.registrar_vehiculo, name='registrar_vehiculo'),
    path('lista-vehiculo/', views.lista_vehiculos, name='lista_vehiculos'),
 ]
