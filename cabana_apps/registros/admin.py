from django.contrib import admin
from .models import ActividadCabana

@admin.register(ActividadCabana)
class ActividadCabanaAdmin(admin.ModelAdmin):
    list_display = ("cabana", "cliente", "descripcion", "fecha")
    search_fields = ("cabana__nombre", "cliente__nombre")
