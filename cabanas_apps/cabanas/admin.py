from django.contrib import admin
from .models import Cabana

# Registrar admin validando que los campos existan en el modelo
desired_list_display = ("nombre", "capacidad", "precio_base", "disponible")
desired_list_filter = ("disponible", "capacidad")
try:
    field_names = {f.name for f in Cabana._meta.get_fields()}
except Exception:
    # En caso de error, usar un fallback conservador
    field_names = set()

safe_list_display = tuple(x for x in desired_list_display if x in field_names)
if not safe_list_display:
    # mínimo visible si no coinciden campos
    safe_list_display = ("nombre", "precio", "disponible")

safe_list_filter = tuple(x for x in desired_list_filter if x in field_names)

@admin.register(Cabana)
class CabanaAdmin(admin.ModelAdmin):
    list_display = safe_list_display
    list_filter = safe_list_filter
    search_fields = tuple(x for x in ("nombre", "descripcion") if x in field_names)
    ordering = ("nombre",)

    # fieldsets: incluir sólo los campos que existan
    basic_fields = tuple(x for x in ("nombre", "capacidad", "descripcion") if x in field_names)
    price_fields = tuple(x for x in ("precio_base", "disponible", "precio") if x in field_names)
    fieldsets = (
        ("Información básica", {"fields": basic_fields}),
        ("Disponibilidad y precio", {"fields": price_fields}),
    )
