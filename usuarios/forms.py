from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from usuarios.models import InfoExtra


class FormularioRegistro(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: '' for k in fields}


class EdicionPerfil(UserChangeForm):
    password = None
    email = forms.EmailField()
    first_name = forms.CharField(label='Nombre', max_length=30)
    last_name = forms.CharField(label='Apellido', max_length=30)

    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'avatar']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'multiple': False}),
        }
        labels = {
            'avatar': 'Imagen de perfil',
        }
        help_texts = {
            'avatar': 'Ingrese una imagen para su perfil (opcional)',
        }
        error_messages = {
            'avatar': {
                'invalid': "Formato de imagen no soportado. Solo se permiten los formatos JPG, PNG, y GIF.",
            }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            info_extra = InfoExtra.objects.get(user=self.instance)
            self.fields['avatar'].initial = info_extra.avatar
        except InfoExtra.DoesNotExist:
            pass

    def save(self, commit=True):
        user = super().save(commit=commit)
        try:
            info_extra = InfoExtra.objects.get(user=user)
        except InfoExtra.DoesNotExist:
            info_extra = InfoExtra(user=user)
        if self.cleaned_data.get('avatar'):
            info_extra.avatar = self.cleaned_data.get('avatar')
        info_extra.save()
        return user