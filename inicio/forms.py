from django import forms
from .models import Vehiculo, Queja

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ('marca', 'modelo', 'anio')

class QuejaForm(forms.ModelForm):
    class Meta:
        model = Queja
        fields = ['queja']