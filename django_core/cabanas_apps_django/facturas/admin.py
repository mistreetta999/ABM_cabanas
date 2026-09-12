from django.contrib import admin
from .models import Factura

@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ("numero", "cliente", "fecha_emision", "monto_total")
    search_fields = ("numero", "cliente__nombre_apellido")
    list_filter = ("fecha_emision",)
