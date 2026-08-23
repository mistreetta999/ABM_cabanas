""" archivo de configuración del panel de administración para el modelo ChatbotResponse """
from django.contrib import admin as interfaz_gestion_cabanas
from .models import ChatbotResponse

@interfaz_gestion_cabanas.register(ChatbotResponse)
class ChatbotResponseAdmin(interfaz_gestion_cabanas.ModelAdmin):
    """ Configuración del panel de administración para el modelo ChatbotResponse """
    list_display = ("chatbot", "message", "created_at")
    search_fields = ("message",)
    list_filter = ("created_at",)
