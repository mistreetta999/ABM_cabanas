"""Administración del modelo ChatbotResponse en el panel de administración de Django."""

from django.contrib import admin

from .models import ChatbotResponse

admin.site.register(ChatbotResponse)
