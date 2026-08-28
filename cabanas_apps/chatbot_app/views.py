"""
Vistas de la aplicación Chatbot.
Permite la interacción con el chatbot, historial y página principal.
"""

from django.views.generic import TemplateView, ListView, FormView
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import ChatMessage
from .forms import ChatForm


class ChatbotHomeView(TemplateView):
    """Vista principal del chatbot."""
    template_name = "chatbot_app/home.html"


class ChatbotInteractView(FormView):
    """Vista para interactuar con el chatbot."""
    template_name = "chatbot_app/interact.html"
    form_class = ChatForm
    success_url = reverse_lazy("chatbot_app:chatbot_interact")

    def form_valid(self, form):
        # Guardar mensaje del usuario
        user_message = form.cleaned_data["message"]
        ChatMessage.objects.create(
            remitente="usuario",
            contenido=user_message
        )

        # Generar respuesta del chatbot (placeholder)
        respuesta = f"🤖 El chatbot recibió: {user_message}"
        ChatMessage.objects.create(
            remitente="chatbot",
            contenido=respuesta
        )

        return super().form_valid(form)


class ChatbotHistoryView(ListView):
    """Vista para mostrar el historial de conversación."""
    model = ChatMessage
    template_name = "chatbot_app/history.html"
    context_object_name = "mensajes"
    ordering = ["-fecha"]
