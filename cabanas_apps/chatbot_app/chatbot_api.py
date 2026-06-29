""" este archivo contiene las rutas URL para la aplicación de chatbot."""

# chatbot_api.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Vista principal del chatbot API
@csrf_exempt
def chatbot_api(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            user_message = data.get("message", "")

            # Respuesta básica (puedes conectar aquí tu lógica con Groq, OpenAI, etc.)
            if "hola" in user_message.lower():
                reply = "¡Hola Carolina 💙! Soy tu chatbot de cabañas."
            elif "reserva" in user_message.lower():
                reply = "Puedes gestionar tu reserva desde el panel de gestión."
            else:
                reply = f"Recibí tu mensaje: {user_message}"

            return JsonResponse({"reply": reply})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Método no permitido"}, status=405)
