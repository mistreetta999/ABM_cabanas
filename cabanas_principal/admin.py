
"""Configuración del panel de administración del proyecto."""

from django.contrib import admin
from django.apps import apps

from cabanas_apps.models import Cliente, Registro, Reserva

Cabana = apps.get_model("cabanas_apps", "Cabana")

# Registrar los modelos en el panel de administración
admin.site.register(Cliente)
admin.site.register(Cabana)
admin.site.register(Reserva)
admin.site.register(Registro)
