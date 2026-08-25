""""Vistas para la aplicación del chatbot."""
from django.shortcuts import render
def panel_chatbot(request):
    """
    Vista que muestra el panel del chatbot.
    """
    context = {
        "titulo": "Panel del Chatbot",
        "descripcion": "Aquí podés interactuar con el chatbot de Cabañas."
    }
    return render(request, "chatbot/panel.html", context)

def chatbot_panel(request):
    """Renderiza el panel del chatbot."""
    return render(request, "chatbot/panel_chatbot.html")

def chatbot_view(request):
    """Renderiza la interfaz principal del chatbot."""
    return render(request, "chatbot/chatbot.html")

def panel_chatbot_respuestas(request):
    """
    Vista que muestra el panel del chatbot.
    """
    context = {
        "titulo": "Panel del Chatbot",
        "descripcion": "Aquí podés interactuar con el chatbot de Cabañas."
    }
    return render(request, "chatbot/panel.html", context)
