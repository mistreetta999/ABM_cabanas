"""Configuración del panel de administración del proyecto."""

from django.contrib import admin

from cabanas_principal.models import (
    Alquiler,
    Cabana,
    Cliente,
    Factura,
    Pago,
    Registro,
    Reserva,
)

# Registrar los modelos en el panel de administración
admin.site.register(Cliente)
admin.site.register(Cabana)
admin.site.register(Reserva)
admin.site.register(Registro)
admin.site.register(Alquiler)
admin.site.register(Pago)
admin.site.register(Factura)
