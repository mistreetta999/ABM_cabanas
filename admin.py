"""Registro de modelos en el panel de administración de Django."""
from django.contrib import admin
from cabanas_api.models import Alquiler, Cabana, Cliente, Reserva, Pago

@admin.register(Alquiler)
class AlquilerAdmin(admin.ModelAdmin):
    """Admin para el modelo Alquiler."""
    list_display = ("id", "cliente", "fecha_inicio", "fecha_fin", "monto")
    list_filter = ("fecha_inicio", "fecha_fin")


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    """Admin para el modelo Cliente."""
    list_display = ("nombre", "email", "usuario")
    search_fields = ("nombre", "email")

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    """Admin para el modelo Reserva."""

    list_display = ("id", "fecha_ingreso", "fecha_salida", "cliente", "cabana", "estado")
    list_filter = ("fecha_ingreso", "fecha_salida", "estado")

@admin.register(Cabana)
class CabanaAdmin(admin.ModelAdmin):
    """Admin para el modelo Cabana."""
    list_display = ("nombre", "capacidad", "precio_por_noche")
    search_fields = ("nombre",)

@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    """Admin para el modelo Pago."""
    list_display = ("id", "alquiler", "monto", "fecha")
    list_filter = ("fecha",)
