from django.contrib import admin
from inicio.models import Vendedor, Comprador, Vehiculo

# Register your models here.

# v1
# admin.site.register(Animal)
# admin.site.register(Persona)

# v2
admin.site.register([Vendedor, Comprador, Vehiculo])