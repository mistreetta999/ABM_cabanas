""" archivo admin"""
from django.contrib import admin
from .models import ActividadCabanas
from django.contrib import admin
from .models import Reserva, Alquiler, Pago, Factura, ActividadCabana

admin.site.register(Reserva)
admin.site.register(Alquiler)
admin.site.register(Pago)
admin.site.register(Factura)
admin.site.register(ActividadCabana)

@admin.register(ActividadCabanas)
class ActividadCabanasAdmin(admin.ModelAdmin):
    """Class actividades cabanas admin"""
    list_display = ("cabana", "cliente", "descripcion", "fecha")
    search_fields = ("cabana__nombre", "cliente__nombre")
