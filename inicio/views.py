from django.http import HttpResponse, HttpResponseBadRequest
from django.template import Template, Context, loader, RequestContext
from inicio.models import Vehiculo, Queja
from django.shortcuts import render, redirect, get_object_or_404
from inicio.forms import VehiculoForm, QuejaForm, BusquedaVehiculoForm
from django.views import View
from django.contrib.auth.mixins import UserPassesTestMixin


class SuperuserRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

class IndexView(View):
    def get(self, request):
        return render(request, 'inicio/index.html')

class AboutView(View):
    def get(self, request):
        return render(request, 'inicio/about.html')

class ListaVehiculosView(View):
    def get(self, request):
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

class AgregarVehiculoView(SuperuserRequiredMixin, View):
    def get(self, request):
        formulario = VehiculoForm()
        return render(request, 'inicio/agregar_vehiculo.html', {'formulario': formulario})

    def post(self, request):
        formulario = VehiculoForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio:lista_vehiculos')
        return render(request, 'inicio/agregar_vehiculo.html', {'formulario': formulario})

class EditarVehiculoView(SuperuserRequiredMixin, View):
    def get(self, request, id_vehiculo):
        vehiculo = get_object_or_404(Vehiculo, id=id_vehiculo)
        formulario = VehiculoForm(instance=vehiculo)
        return render(request, 'inicio/editar_vehiculo.html', {'formulario': formulario, 'id_vehiculo': id_vehiculo})

    def post(self, request, id_vehiculo):
        vehiculo = get_object_or_404(Vehiculo, id=id_vehiculo)
        formulario = VehiculoForm(request.POST, request.FILES, instance=vehiculo)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio:lista_vehiculos')
        return render(request, 'inicio/editar_vehiculo.html', {'formulario': formulario, 'id_vehiculo': id_vehiculo})

class EliminarVehiculoView(SuperuserRequiredMixin, View):
    def get(self, request, id_vehiculo):
        vehiculo = get_object_or_404(Vehiculo, id=id_vehiculo)
        return render(request, 'inicio/eliminar_vehiculo.html', {'vehiculo': vehiculo})
    
    def post(self, request, id_vehiculo):
        vehiculo = get_object_or_404(Vehiculo, id=id_vehiculo)
        vehiculo.delete()
        return redirect('inicio:lista_vehiculos')

class DetalleVehiculoView(View):
    def get(self, request, id_vehiculo):
        vehiculo = get_object_or_404(Vehiculo, id=id_vehiculo)
        return render(request, 'inicio/detalle_vehiculo.html', {'vehiculo': vehiculo})

class ListaQuejasView(View):
    def get(self, request):
        quejas = Queja.objects.all()
        return render(request, 'inicio/lista_quejas.html', {'quejas': quejas})

class AgregarQuejaView(View):
    def get(self, request):
        form = QuejaForm()
        context = {'form': form}
        return render(request, 'inicio/agregar_queja.html', context)
    
    def post(self, request):
        form = QuejaForm(request.POST)
        if form.is_valid():
            queja = form.save(commit=False)
            queja.save()
            return redirect('inicio:lista_quejas')
        context = {'form': form}
        return render(request, 'inicio/agregar_queja.html', context)
