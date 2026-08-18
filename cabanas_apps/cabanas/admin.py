from django.contrib import admin
from .models import Cabanas


@admin.register(Cabanas
)
class CabanaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "capacidad", "precio_por_noche")
