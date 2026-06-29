# cabanas_apps/chatbot_app/chatbot/chatbot_panel.py

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
