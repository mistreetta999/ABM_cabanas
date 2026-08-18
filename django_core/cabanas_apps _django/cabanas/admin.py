from django.contrib import admin as interfaz_gestion_cabanas
from .models import Cabanas


@interfaz_gestion_cabanas.register(Cabanas
)
class CabanaAdmin(interfaz_gestion_cabanas.ModelAdmin):
    list_display = ("nombre", "capacidad", "precio_por_noche", "disponible")
    search_fields = ("nombre",)
