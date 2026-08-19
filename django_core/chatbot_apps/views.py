""" views de la app chatbot
"""
from django.shortcuts import render
from django.http import JsonResponse

def chatbot_home(request):
    """Renderiza la página principal del chatbot.
    """
    return render(request, "chatbot/panel.html")

def chatbot_ask(request):
    """Maneja las preguntas enviadas al chatbot y devuelve una respuesta.
    """
    if request.method == "POST":
        pregunta = request.POST.get("pregunta", "")
        # Aquí iría la lógica de respuesta del bot
        return JsonResponse({"respuesta": f"Recibí tu pregunta: {pregunta}"})
    return JsonResponse({"error": "Método no permitido"})
