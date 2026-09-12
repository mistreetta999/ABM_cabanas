""" archivo interfaz_gestion_cabanas"""
from django.contrib import admin
from .models import Registro

@admin.register(Registro)
class RegistroAdmin(admin.ModelAdmin):
    list_display = ("reserva", "cliente", "fecha_registro", "detalle")
    search_fields = ("detalle", "cliente__nombre_apellido")
    list_filter = ("fecha_registro",)






