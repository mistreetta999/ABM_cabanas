""" archivo de configuración del panel de administración para el modelo ChatbotResponse """
from django.contrib import admin
from .models import ChatbotResponse

@admin.register(ChatbotResponse)
class ChatbotResponseAdmin(admin.ModelAdmin):
    """ Configuración del panel de administración para el modelo ChatbotResponse """
    list_display = ("pregunta", "respuesta")   # columnas visibles en el admin
    search_fields = ("pregunta", "respuesta")  # barra de búsqueda
    list_filter = ("pregunta",)                # filtros laterales
