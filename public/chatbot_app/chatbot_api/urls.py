"""URLs de la API del Chatbot (pública)."""

from django.urls import path
from . import views

app_name = "chatbot_api"

urlpatterns = [
    # Endpoint para enviar mensajes al chatbot
    path("send/", views.api_send_message, name="api_send_message"),

    # Endpoint para obtener respuesta del chatbot
    path("response/", views.api_get_response, name="api_get_response"),

    # Endpoint para historial de conversaciones
    path("history/", views.api_get_history, name="api_get_history"),

    # Endpoint para limpiar historial
    path("clear/", views.api_clear_history, name="api_clear_history"),
]
