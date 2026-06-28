from django.contrib import admin
from .models import Cabana


@admin.register(Cabana)
class CabanaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'capacidad', 'precio_dia', 'habilitada', 'ocupada')
    search_fields = ('nombre',)
