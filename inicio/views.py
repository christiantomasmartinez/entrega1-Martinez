from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.template import Template, Context, loader, RequestContext
from inicio.models import Vehiculo
from django.shortcuts import render, redirect, get_object_or_404
from inicio.forms import VehiculoForm


def mi_vista(request):
    return render(request, 'inicio/index.html')

def about(request):
    return render(request, 'inicio/about.html')

def lista_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'inicio/lista_vehiculos.html', {'vehiculos': vehiculos})

def agregar_vehiculo(request):
    if request.method == 'POST':
        formulario = VehiculoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio:lista_vehiculos')
    else:
        formulario = VehiculoForm()
    return render(request, 'inicio/agregar_vehiculo.html', {'formulario': formulario})

def editar_vehiculo(request, id_vehiculo):
    vehiculo = get_object_or_404(Vehiculo, id=id_vehiculo)
    if request.method == 'POST':
        formulario = VehiculoForm(request.POST, instance=vehiculo)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio:lista_vehiculos')
    else:
        formulario = VehiculoForm(instance=vehiculo)
    return render(request, 'inicio/editar_vehiculo.html', {'formulario': formulario, 'id_vehiculo': id_vehiculo})

def eliminar_vehiculo(request, id_vehiculo):
    vehiculo = get_object_or_404(Vehiculo, id=id_vehiculo)
    if request.method == 'POST':
        vehiculo.delete()
        return redirect('inicio:lista_vehiculos')
    return render(request, 'inicio/eliminar_vehiculo.html', {'vehiculo': vehiculo})