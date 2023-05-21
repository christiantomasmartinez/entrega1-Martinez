from django.urls import path
from .views import *

app_name = 'inicio'

urlpatterns = [
    path('', IndexView.as_view(), name='inicio'),
    path('about/', AboutView.as_view(), name='about'),
    path('lista_vehiculos/', ListaVehiculosView.as_view(), name='lista_vehiculos'),
    path('agregar_vehiculo/', AgregarVehiculoView.as_view(), name='agregar_vehiculo'),
    path('editar_vehiculo/<int:id_vehiculo>/', EditarVehiculoView.as_view(), name='editar_vehiculo'),
    path('eliminar_vehiculo/<int:id_vehiculo>/', EliminarVehiculoView.as_view(), name='eliminar_vehiculo'),
    path('detalle_vehiculo/<int:id_vehiculo>/', DetalleVehiculoView.as_view(), name='detalle_vehiculo'),
    path('lista_quejas/', ListaQuejasView.as_view(), name='lista_quejas'),
    path('agregar_queja/', AgregarQuejaView.as_view(), name='agregar_queja'),
]