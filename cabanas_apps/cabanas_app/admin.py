""" Archivo de configuración del panel de administración de Django para registrar modelos. """
from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    """Clase de administración para el modelo Cliente, que define cómo se muestran los registros de clientes en el panel de administración de Django."""
    list_display = ("nombre", "apellido", "email", "telefono", "fecha_registro")
    search_fields = ("nombre", "apellido", "email")
