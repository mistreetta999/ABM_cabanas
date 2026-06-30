""" archivo admin.py para registrar los modelos en el panel de administración de Django """
from django.contrib import admin
from registros.models import Reserva, Alquiler, Pago, Factura, ActividadCabana

# Registrar cada modelo en el panel de administración
admin.site.register(Reserva)
admin.site.register(Alquiler)
admin.site.register(Pago)
admin.site.register(Factura)
admin.site.register(ActividadCabana)
