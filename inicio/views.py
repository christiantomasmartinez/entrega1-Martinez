from django.http import HttpResponse, HttpResponseBadRequest
from django.template import Template, Context, loader, RequestContext
from inicio.models import Vehiculo, Queja
from django.shortcuts import render, redirect, get_object_or_404
from inicio.forms import VehiculoForm, QuejaForm, BusquedaVehiculoForm
from django.contrib.auth.decorators import user_passes_test


def mi_vista(request):
    return render(request, 'inicio/index.html')

def about(request):
    return render(request, 'inicio/about.html')

def lista_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    form = BusquedaVehiculoForm(request.GET)
    if form.is_valid():
        marca = form.cleaned_data['marca']
        modelo = form.cleaned_data['modelo']
        anio = form.cleaned_data['anio']
        
        if marca:
            vehiculos = vehiculos.filter(marca__icontains=marca)
        if modelo:
            vehiculos = vehiculos.filter(modelo__icontains=modelo)
        if anio:
            vehiculos = vehiculos.filter(anio=anio)
    
    context = {
        'form': form,
        'vehiculos': vehiculos,
    }
    return render(request, 'inicio/lista_vehiculos.html', context)


@user_passes_test(lambda u: u.is_superuser)
def agregar_vehiculo(request):
    if request.method == 'POST':
        formulario = VehiculoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio:lista_vehiculos')
    else:
        formulario = VehiculoForm()
    return render(request, 'inicio/agregar_vehiculo.html', {'formulario': formulario})

@user_passes_test(lambda u: u.is_superuser)
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

@user_passes_test(lambda u: u.is_superuser)
def eliminar_vehiculo(request, id_vehiculo):
    vehiculo = get_object_or_404(Vehiculo, id=id_vehiculo)
    if request.method == 'POST':
        vehiculo.delete()
        return redirect('inicio:lista_vehiculos')
    return render(request, 'inicio/eliminar_vehiculo.html', {'vehiculo': vehiculo})

def lista_quejas(request):
    quejas = Queja.objects.all()
    return render(request, 'inicio/lista_quejas.html', {'quejas': quejas})


def agregar_queja(request):
    if request.method == 'POST':
        form = QuejaForm(request.POST)
        if form.is_valid():
            queja = form.save(commit=False)
            queja.save()
            return redirect('inicio:lista_quejas')
    else:
        form = QuejaForm()
    context = {'form': form}
    return render(request, 'inicio/agregar_queja.html', context)