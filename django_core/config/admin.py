"""ädmin"""

from django.apps import apps
from django.contrib import admin

from cabanas_api.models import Cliente

Alquiler = apps.get_model("cabanas_api", "Alquiler")


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    """Admin para gestionar clientes."""

    list_display = ("nombre", "dni", "telefono", "email")
    search_fields = ("nombre", "dni")


@admin.register(Alquiler)
class AlquilerAdmin(admin.ModelAdmin):
    """Admin para gestionar alquileres."""

    list_display = ("cliente", "fecha_ingreso", "fecha_salida", "estado", "monto_total")
    list_filter = ("estado", "fecha_ingreso", "fecha_salida")
