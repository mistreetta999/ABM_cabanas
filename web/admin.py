from django.contrib import admin as interfaz_gestion_cabanas

from .models import Publicacion


@interfaz_gestion_cabanas.register(Publicacion)
class PublicacionAdmin(interfaz_gestion_cabanas.ModelAdmin):
    list_display = ("titulo", "creado_en")
    search_fields = ("titulo", "descripcion")
