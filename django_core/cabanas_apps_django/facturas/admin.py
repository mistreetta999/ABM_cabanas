from django.contrib import admin

from django_core.cabanas_apps_django.facturas.models import Factura


@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ("numero", "fecha_emision", "total")
