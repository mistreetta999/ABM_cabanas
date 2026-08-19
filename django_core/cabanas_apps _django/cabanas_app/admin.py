""" Archivo de configuración del panel de administración de Django para registrar modelos. """
from django.contrib import admin as interfaz_gestion_cabanas
from .models import Cliente

@interfaz_gestion_cabanas.register(Cliente)
class ClienteAdmin(interfaz_gestion_cabanas.ModelAdmin):
    """Clase de administración para el modelo Cliente, que define cómo se muestran los registros de clientes en el panel de administración de Django."""
    list_display = ("nombre", "apellido", "email", "telefono", "fecha_registro")
    search_fields = ("nombre", "apellido", "email")
