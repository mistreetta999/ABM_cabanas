from django.contrib import admin
from .models import Cabana

@admin.register(Cabana)
class CabanaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "capacidad", "precio_por_noche", "disponible")
    search_fields = ("nombre",)
