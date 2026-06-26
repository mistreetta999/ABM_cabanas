from django.contrib import admin
from .models import Reserva

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ("cliente", "cabana", "fecha_inicio", "fecha_fin", "estado")
    search_fields = ("cliente__nombre", "cabana__nombre")
