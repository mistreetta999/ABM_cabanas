""" Admin configuration for the pagos app."""
from django.contrib import admin
from .models import Pago

@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin): 
    """Class pagos admin"""
    list_display = ("id", "fecha_pago", "monto")
    print("Vista de Pagos")
