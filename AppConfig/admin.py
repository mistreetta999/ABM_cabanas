"""Configuración del panel de administración para AppConfig."""

from django.contrib import admin

from .models import Configuracion


@admin.register(Configuracion)
class ConfiguracionAdmin(admin.ModelAdmin):
    list_display = ("nombre", "valor", "activo")
    search_fields = ("nombre", "valor")
    list_filter = ("activo",)
    ordering = ("nombre",)

    fieldsets = (
        ("Información básica", {"fields": ("nombre", "valor")}),
        ("Estado", {"fields": ("activo",)}),
    )
