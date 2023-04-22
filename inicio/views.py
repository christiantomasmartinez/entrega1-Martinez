from django.http import HttpResponse
from django.template import Template, Context, loader
from inicio.models import Vehiculo
from django.shortcuts import render, redirect
from inicio.forms import CreacionVehiculoFormulario, BuscarAuto



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
        
            vehiculo = Vehiculo(modelo=datos_correctos['modelo'], marca=datos_correctos['marca'], kilometraje=datos_correctos["kilometraje"])
            vehiculo.save()

            return redirect('inicio:registrar_vehiculo')
    
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