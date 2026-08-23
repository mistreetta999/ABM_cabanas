from django.contrib import admin as interfaz_gestion_cabanas
from .models import Cabanas



@interfaz_gestion_cabanas.register(Cabanas
)
class CabanaAdmin(interfaz_gestion_cabanas.ModelAdmin):
    list_display = ('id', 'nombre', 'capacidad', 'precio_dia', 'habilitada', 'ocupada')
    search_fields = ('nombre',)
