""" archivo de urls del proyecto """
from django.contrib import admin as interfaz_gestion_cabanas
from .models import Cliente

@interfaz_gestion_cabanas.register(Cliente)
class ClienteAdmin(interfaz_gestion_cabanas.ModelAdmin):
    """interfaz_gestion_cabanas class for the Cliente model."""
    list_display = ("nombre", "apellido", "dni", "telefono")
    search_fields = ("nombre", "apellido", "dni")
    list_filter = ("apellido",)
