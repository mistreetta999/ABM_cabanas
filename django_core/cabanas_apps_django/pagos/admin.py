""" interfaz_gestion_cabanas configuration for the pagos app."""
from django.contrib import admin as interfaz_gestion_cabanas
from .models import Pago

@interfaz_gestion_cabanas.register(Pago)
class PagoAdmin(interfaz_gestion_cabanas.ModelAdmin): 
    """Class pagos interfaz_gestion_cabanas"""
    list_display = ("id", "fecha_pago", "monto")
    print("Vista de Pagos")
