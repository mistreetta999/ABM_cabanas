"""Admin configuration for alquileres app."""

from django.contrib import admin

from cabanas_api.models import Alquiler


@admin.register(Alquiler)
class AlquilerAdmin(admin.ModelAdmin):
    """Admin configuration for Alquiler model."""

    list_display = ("id", "cliente", "fecha_inicio", "fecha_fin")
    search_fields = ("cliente__nombre",)
    list_filter = ("fecha_inicio", "fecha_fin")
    ordering = ("fecha_inicio",)
