from django.db import models

class Vehiculo(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.IntegerField()
    imagen = models.ImageField(upload_to='vehiculos/', null=True, blank=True)
    descripcion = models.TextField(default='Sin descripcion')

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.anio})"



class Queja(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    queja = models.TextField()