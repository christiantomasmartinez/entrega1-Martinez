from django.db import models

# Create your models here.

class Vendedor(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    meses_de_contrato = models.IntegerField()
    
    def __str__(self):
        return f'Soy {self.nombre} {self.apellido}, y trabajare aqui por {self.meses_de_contrato} meses.'
    
class Comprador(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    
    def __str__(self):
        return f'Soy {self.nombre} {self.apellido}'

class Vehiculo(models.Model):
    modelo = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    kilometraje = models.IntegerField()
    
    def __str__(self):
        return f'Vehiculo: {self.marca} {self.modelo} {self.kilometraje}km.'