from django import forms


class CreacionVehiculoFormulario(forms.Form):
    modelo = forms.CharField(max_length=20)
    marca = forms.CharField(max_length=20)
    kilometraje = forms.IntegerField()

class BuscarAuto(forms.Form):
    modelo = forms.CharField(max_length=20, required=False)