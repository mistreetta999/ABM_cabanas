"""Este archivo contiene las vistas de la app registros."""
from django.shortcuts import render


def chatbot_view(request):
    """Vista para el chatbot."""
    return render(request, "chatbot/chat.html")
