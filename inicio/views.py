from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.template import Template, Context, loader, RequestContext
from inicio.models import Vehiculo
from django.shortcuts import render, redirect
from inicio.forms import CreacionVehiculoFormulario, BuscarAuto
from django.contrib import messages


def mi_vista(request):
    return render(request, 'inicio/index.html')

def about(request):
    return render(request, 'inicio/about.html')

def registro_exitoso(request):
    return render(request, 'inicio/registro_exitoso.html')

def registrar_vehiculo(request):
    if request.method == "POST":
        formulario = CreacionVehiculoFormulario(request.POST)
        
        if formulario.is_valid():
            datos_correctos = formulario.cleaned_data
        
            vehiculo = Vehiculo(
                modelo=datos_correctos['modelo'], 
                marca=datos_correctos['marca'], 
                kilometraje=datos_correctos["kilometraje"]
            )
            vehiculo.save()
            messages.success(request, 'Vehículo registrado correctamente.')
            return redirect('inicio:registro_exitoso')
        else:
            messages.error(request, 'Error al procesar el formulario.')
    else:
        formulario = CreacionVehiculoFormulario()
    
    return render(request, 'inicio/registrar_vehiculo.html', {'formulario': formulario})

def lista_vehiculos(request):
    modelo_a_buscar = request.GET.get('modelo', None)

    if modelo_a_buscar:
        vehiculo = Vehiculo.objects.filter(modelo__icontains=modelo_a_buscar)
    else:
        vehiculo = Vehiculo.objects.all()
    formulario_busqueda = BuscarAuto()
    return render(request, 'inicio/lista_vehiculos.html', {'vehiculos': vehiculo, 'formulario': formulario_busqueda})

def eliminar_vehiculo(request):
    if request.method == 'POST':
        id_vehiculo = request.POST.get('id_vehiculo', None)
        vehiculo = Vehiculo.objects.get(id=id_vehiculo)
        vehiculo.delete()
        return redirect('inicio:lista_vehiculos')
    else:
        return HttpResponseBadRequest('Método no permitido')

from django.shortcuts import get_object_or_404

def editar_vehiculo(request, id_vehiculo):
    vehiculo = get_object_or_404(Vehiculo, id=id_vehiculo)
    formulario = CreacionVehiculoFormulario(initial={"modelo":"GOT"})
    
    if request.method == "POST":
        formulario = CreacionVehiculoFormulario(request.POST)
        
        if formulario.is_valid():
            vehiculo = Vehiculo()
            
            vehiculo.marca = formulario.cleaned_data["marca"]
            vehiculo.modelo = formulario.cleaned_data["modelo"]
            vehiculo.kilometraje = formulario.cleaned_data["kilometraje"]
            
            vehiculo.save()
            
            messages.success(request, 'Vehículo registrado correctamente.')
            return redirect('inicio:registro_exitoso')
        else:
            messages.error(request, 'Error al procesar el formulario.')
    else:
        formulario = CreacionVehiculoFormulario()
    
    return render(request, 'inicio/registrar_vehiculo.html', {'formulario': formulario})
