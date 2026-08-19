""" interfaz_gestion_cabanas configuration for the chatbot_apps application. """

from django.contrib import admin as interfaz_gestion_cabanas
from cabanas_apps.chatbot_app.models import Chatbot

@interfaz_gestion_cabanas.register(Chatbot)
class ChatbotAdmin(interfaz_gestion_cabanas.ModelAdmin):
    """ interfaz_gestion_cabanas configuration for the Chatbot model. """
    list_display = ("id", "nombre", "descripcion")
    search_fields = ("nombre",)
    list_filter = ("nombre",)
    fieldsets = (
        (None, {"fields": ("nombre", "descripcion")}),
    )