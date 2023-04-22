from django.db import models

# Create your models here.

class Vehiculo(models.Model):
    modelo = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    kilometraje = models.IntegerField()
    
    def __str__(self):
        return f'Vehiculo: {self.marca} {self.modelo} {self.kilometraje}km.'