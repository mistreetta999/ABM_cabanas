"""interfaz_gestion_cabanas configuracion  para Reserva models."""
from django.contrib import admin as interfaz_gestion_cabanas
from .models import Reserva

@interfaz_gestion_cabanas.register(Reserva)
class ReservaAdmin(interfaz_gestion_cabanas.ModelAdmin):
    """interfaz_gestion_cabanas configuracion para el modelo Reserva."""
    list_display = ("cliente", "Cabanas
", "fecha_inicio", "fecha_fin", "estado")
    search_fields = ("cliente__nombre", "cabana__nombre")
