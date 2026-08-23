""" archivo interfaz_gestion_cabanas"""
from django.contrib import admin as interfaz_gestion_cabanas
from .models import ActividadCabanas

@interfaz_gestion_cabanas.register(ActividadCabanas)
class ActividadCabanasAdmin(interfaz_gestion_cabanas.ModelAdmin):
    """Class actividades cabanas interfaz_gestion_cabanas"""
    list_display = ("Cabanas
", "cliente", "descripcion", "fecha")
    search_fields = ("cabana__nombre", "cliente__nombre")
