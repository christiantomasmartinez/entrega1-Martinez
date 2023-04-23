from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.mi_vista, name='inicio'),
    path('about/', views.about, name='about'),
    path('agregar/', views.agregar_vehiculo, name='agregar_vehiculo'),
    path('editar/<int:id_vehiculo>/', views.editar_vehiculo, name='editar_vehiculo'),
    path('eliminar/<int:id_vehiculo>/', views.eliminar_vehiculo, name='eliminar_vehiculo'),
    path('lista-vehiculos/', views.lista_vehiculos, name='lista_vehiculos'),
]