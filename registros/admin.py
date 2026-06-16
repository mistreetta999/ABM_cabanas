from django.contrib import admin

from .models import Cabana, RegistroDiario


@admin.register(Cabana)
class CabanaRegistroAdmin(admin.ModelAdmin):
    list_display = ("nombre", "capacidad_clientes", "precio_por_noche", "esta_activa")
    search_fields = ("nombre",)
    list_filter = ("esta_activa",)


@admin.register(RegistroDiario)
class RegistroDiarioAdmin(admin.ModelAdmin):
    list_display = (
        "cabana",
        "cabana_gestion",
        "cabana_reservas",
        "reserva_gestion",
        "reserva",
        "fecha",
        "fue_limpiada",
    )
    list_filter = ("fue_limpiada", "fecha")
    search_fields = (
        "cabana__nombre",
        "cabana_gestion__nombre",
        "cabana_reservas__nombre",
        "novedades",
    )
    raw_id_fields = (
        "cabana_gestion",
        "cabana_reservas",
        "reserva_gestion",
        "reserva",
    )
