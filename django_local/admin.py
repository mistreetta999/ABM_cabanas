"""este es el archivo admin"""
from django.contrib import admin
from django.Models.model import models
from django.Moodels.models import Cabana
from django.Models.models import  Cliente
from django.Models.models import  Registros
from django.Models.models import   Reserva
from django.models import Pagos
from cabanas.modelcabanas import admin

class admin:
def __init__(self):
    self.admin.site.register(Cliente)
    self.admin.site.register(Cabana)
    self.admin.site.register(Factura)
    self.admin.site.register(Reservas)
    self.admin.site.register(Alquileres)
    self.admin.site.register(Pago)

# Register  models 
admin.site.register(Cliente)
admin.site.register(Cabana)
admin.site.register(Factura)
admin.site.register(Reservas)
admin.site.register(Alquileres)
admin.site.register(Pago)

# Registrar los modelos en el panel de administración
admin.site.register(Cliente)
admin.site.register(Reserva)
admin.site.register(Servicio)
admin.site.register(Pago)
