""" archivo interfaz_gestion_cabanas"""
from django.contrib import admin as interfaz_gestion_cabanas
from .models import Registro

@interfaz_gestion_cabanas.register(Registro)
class RegistroAdmin(interfaz_gestion_cabanas.ModelAdmin):
    """ Class registro interfaz_gestion_cabanas"""
    list_display = ("accion", "usuario", "fecha")
    search_fields = ("accion", "descripcion", "usuario__username")
