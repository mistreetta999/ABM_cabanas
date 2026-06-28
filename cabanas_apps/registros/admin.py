""" archivo admin"""
from django.contrib import admin
from .models import ActividadCabanas

@admin.register(ActividadCabanas)
class ActividadCabanasAdmin(admin.ModelAdmin):
    """Class actividades cabanas admin"""
    list_display = ("cabana", "cliente", "descripcion", "fecha")
    search_fields = ("cabana__nombre", "cliente__nombre")
