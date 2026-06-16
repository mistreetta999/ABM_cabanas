# chatbot/chatbot_views.py

from django.shortcuts import render
from django.http import JsonResponse
class ChatbotView:
 def __init__(self, request):
        self.request = request

# Vista principal del chatbot (para el iframe)
def chatbot_view(request):
    """
    Renderiza la interfaz del chatbot.
    """
    return render(request, "chatbot/chat.html")


# Ejemplo de endpoint para procesar mensajes del chatbot
def chatbot_api(request):
    """
    Endpoint que recibe mensajes del usuario y devuelve una respuesta simulada.
    Más adelante puedes conectarlo con tu lógica real (FastAPI, Telegram, etc.).
    """
    if request.method == "POST":
        user_message = request.POST.get("message", "")
        # Aquí podrías llamar a tu bot o lógica de IA
        response = f"Recibí tu mensaje: {user_message}"
        return JsonResponse({"reply": response})
    return JsonResponse({"error": "Método no permitido"}, status=405)
