""" views del chatbot"""
from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

def chatbot_home(request):
    return HttpResponse("Bienvenidos, este es el panel del Chatbot.")

@csrf_exempt
def chatbot_api(request):
    if request.method == "POST":
        user_message = request.POST.get("message", "")
        # Aquí podrías conectar con tu lógica de chatbot
        response = f"Respuesta automática a: {user_message}"
        return JsonResponse({"response": response})
    return JsonResponse({"error": "Método no permitido"}, status=405)


def index(request):
    return render(request, "chatbot/index.html")
