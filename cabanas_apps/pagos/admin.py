""" interfaz_gestion_cabanas configuration for the pagos app."""
from django.contrib import admin
from .models import Pago

@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ("id", "alquiler", "fecha", "monto", "metodo")
    list_filter = ("metodo", "fecha")
