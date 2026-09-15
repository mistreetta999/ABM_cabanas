"""admin"""

from django.contrib import admin

from .models import Cabana


@admin.register(Cabana)
class CabanaAdmin(admin.ModelAdmin):
    list_display = ("nombre",)  # solo campos que existan en el modelo
    search_fields = ("nombre",)
