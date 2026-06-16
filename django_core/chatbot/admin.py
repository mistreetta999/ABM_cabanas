from django.contrib import admin
from chatbot.models import Chatbot

@admin.register(Chatbot)
class ChatbotAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "descripcion")
    search_fields = ("nombre",)
    list_filter = ("nombre",)
    fieldsets = (
        (None, {"fields": ("nombre", "descripcion")}),
    )