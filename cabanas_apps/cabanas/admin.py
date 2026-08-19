from django.contrib import admin
from .models import Cabana

@admin.register(Cabana)
class CabanaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "capacidad", "precio_base", "disponible")
    list_filter = ("disponible", "capacidad")
    search_fields = ("nombre", "descripcion")
    ordering = ("nombre",)

    fieldsets = (
        ("Información básica", {
            "fields": ("nombre", "capacidad", "descripcion")
        }),
        ("Disponibilidad y precio", {
            "fields": ("precio_base", "disponible")
        }),
    )
