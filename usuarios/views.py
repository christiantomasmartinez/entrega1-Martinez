from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as login_django
from usuarios.forms import FormularioRegistro, EdicionPerfil, DescripcionForm, EnlaceForm
from django.contrib.auth.decorators import login_required
from usuarios.models import InfoExtra
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView



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
            usuario = formulario.save()  # Guardar el usuario
            InfoExtra.objects.get_or_create(user=usuario)  # Crear el objeto InfoExtra para el usuario
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
            formulario.save()
            infoextra = request.user.infoextra
            if 'avatar' in request.FILES:
                infoextra.avatar = request.FILES['avatar']
            infoextra.save()
            return redirect('usuarios:editar_perfil')
        else:
            return render(request, 'usuarios/editar_perfil.html', {'form': formulario})
    formulario = EdicionPerfil(instance=request.user)
    return render(request, 'usuarios/editar_perfil.html', {'form': formulario})


class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = 'usuarios/cambiar_contrasenia.html'
    success_url = reverse_lazy('usuarios:editar_perfil')



@login_required
def perfil_usuario(request, username):
    perfil = get_object_or_404(InfoExtra, user__username=username)
    return render(request, 'usuarios/perfil.html', {'perfil': perfil})


def editar_descripcion(request, username):
    # Obtener el perfil del usuario actual
    perfil = get_object_or_404(InfoExtra, user__username=username)

    if request.method == 'POST':
        form = DescripcionForm(request.POST, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('usuarios:perfil', username=username)
    else:
        form = DescripcionForm(instance=perfil)

    return render(request, 'usuarios/editar_descripcion.html', {'form': form})

from django.shortcuts import render, redirect, get_object_or_404
from .forms import DescripcionForm, EnlaceForm
from usuarios.models import InfoExtra


def editar_enlace(request, username):
    # Obtener el perfil del usuario actual
    perfil = get_object_or_404(InfoExtra, user__username=username)

    if request.method == 'POST':
        form = EnlaceForm(request.POST, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('usuarios:perfil', username=username)
    else:
        form = EnlaceForm(instance=perfil)

    return render(request, 'usuarios/editar_enlace.html', {'form': form})

