from django.contrib import admin
from .models import GestionLog

@admin.register(GestionLog)
class GestionLogAdmin(admin.ModelAdmin):
    list_display = ("usuario", "accion", "fecha")
    search_fields = ("usuario", "accion")
