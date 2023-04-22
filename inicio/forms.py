from django import forms


class CreacionCompradorFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)

class CreacionVendedorFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    meses_de_contrato = forms.IntegerField()
    
class CreacionVehiculoFormulario(forms.Form):
    modelo = forms.CharField(max_length=20)
    marca = forms.CharField(max_length=20)
    kilometraje = forms.IntegerField()
    
class BuscarAuto(forms.Form):
    modelo = forms.CharField(max_length=20, required=False)