from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as login_django
from usuarios.forms import FormularioRegistro, EdicionPerfil
from django.contrib.auth.decorators import login_required
from usuarios.models import InfoExtra
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def login(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contrasenia = formulario.cleaned_data.get('password')
            
            user = authenticate(username=usuario, password=contrasenia)
            
            login_django(request, user)
            
            InfoExtra.objects.get_or_create(user=user)
            
            return redirect('inicio:inicio')
        else:
            return render(request, 'usuarios/login.html', {'form': formulario})
    
    formulario = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form': formulario})

def registro(request):
    
    if request.method == 'POST':
        formulario = FormularioRegistro(request.POST)
        
        if formulario.is_valid():
            formulario.save()
            
            return redirect('usuarios:login')
        else:
            return render(request, 'usuarios/registro.html', {'form': formulario})
    
    formulario = FormularioRegistro()
    return render(request, 'usuarios/registro.html', {'form': formulario})
    
@login_required
def editar_perfil(request):
    
    if request.method == 'POST':
        formulario = EdicionPerfil(request.POST, request.FILES, instance=request.user)
        
        if formulario.is_valid():
            
            if formulario.cleaned_data.get('avatar'):
                request.user.infoextra.avatar = formulario.cleaned_data.get('avatar')
                request.user.infoextra.save()
            
            formulario.save()
            
            return redirect('usuarios:editar_perfil')
        else:
            return render(request, 'usuarios/editar_perfil.html', {'form': formulario})
    
    formulario = EdicionPerfil(initial={'avatar': request.user.infoextra.avatar}, instance=request.user)
    return render(request, 'usuarios/editar_perfil.html', {'form': formulario})

class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = 'usuarios/cambiar_contrasenia.html'
    success_url = reverse_lazy('usuarios:editar_perfil')