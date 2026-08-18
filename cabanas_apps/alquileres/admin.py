""" archivo interfaz_gestion_cabanas"""
from django.contrib import admin as interfaz_gestion_cabanas
from .models import Alquiler

@interfaz_gestion_cabanas.register(Alquiler)
class AlquilerAdmin(interfaz_gestion_cabanas.ModelAdmin):
    """interfaz_gestion_cabanas class for the Alquiler model."""
    list_display = ("id", "cliente", "cabanas", "reservas", "monto_total", "fecha_pago")
    list_filter = ("fecha_pago",)
