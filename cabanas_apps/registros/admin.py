""" archivo admin"""
from django.contrib import admin
from .models import Registro

@admin.register(Registro)
class RegistroAdmin(admin.ModelAdmin):
    """ Class registro admin"""
    list_display = ("accion", "usuario", "fecha")
    search_fields = ("accion", "descripcion", "usuario__username")
