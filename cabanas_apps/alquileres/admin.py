""" archivo interfaz_gestion_cabanas"""
from django.contrib import admin as interfaz_gestion_cabanas
from .models import Alquiler

# Registrar admin validando que los campos existan en el modelo
from django.db import models as _dj_models

desired_list_display = ("id", "cliente", "cabanas", "reservas", "monto_total", "fecha_pago")
try:
    field_names = {f.name for f in Alquiler._meta.get_fields()}
except Exception:
    field_names = set()

safe_list_display = tuple(x for x in desired_list_display if x in field_names)
if not safe_list_display:
    safe_list_display = ("id", "cliente", "monto_total", "fecha_pago")

@interfaz_gestion_cabanas.register(Alquiler)
class AlquilerAdmin(interfaz_gestion_cabanas.ModelAdmin):
    list_display = safe_list_display
    list_filter = tuple(x for x in ("fecha_pago",) if x in field_names)
