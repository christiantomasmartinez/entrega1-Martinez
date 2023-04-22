from django.http import HttpResponse
from django.template import Template, Context, loader
from inicio.models import Vendedor, Comprador, Vehiculo
from django.shortcuts import render, redirect
from inicio.forms import CreacionCompradorFormulario, CreacionVendedorFormulario, CreacionVehiculoFormulario, BuscarAuto



def mi_vista(request):
    return render(request, 'inicio/index.html')

def registrar_comprador(request):
    
    if request.method == "POST":
        formulario = CreacionCompradorFormulario(request.POST)
        
        if formulario.is_valid():
            datos_correctos = formulario.cleaned_data
        
            comprador = Comprador(nombre=datos_correctos['nombre'], apellido=datos_correctos['apellido'])
            comprador.save()

            return redirect('inicio:registrar_comprador')
    
    formulario = CreacionCompradorFormulario()
    return render(request, 'inicio/registrar_comprador.html', {'formulario': formulario})

def registrar_vendedor(request):
    
    if request.method == "POST":
        formulario = CreacionVendedorFormulario(request.POST)
        
        if formulario.is_valid():
            datos_correctos = formulario.cleaned_data
        
            vendedor = Vendedor(nombre=datos_correctos['nombre'], apellido=datos_correctos['apellido'], meses_de_contrato=datos_correctos["meses_de_contrato"])
            vendedor.save()

            return redirect('inicio:registrar_vendedor')
    
    formulario = CreacionVendedorFormulario()
    return render(request, 'inicio/registrar_vendedor.html', {'formulario': formulario}) 

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

def registro_exitoso(request):
    return render(request, 'inicio/registro_exitoso.html')