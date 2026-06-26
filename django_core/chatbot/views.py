from django.shortcuts import render
from django.http import JsonResponse

def chatbot_home(request):
    return render(request, "chatbot/panel.html")

def chatbot_ask(request):
    if request.method == "POST":
        pregunta = request.POST.get("pregunta", "")
        # Aquí iría la lógica de respuesta del bot
        return JsonResponse({"respuesta": f"Recibí tu pregunta: {pregunta}"})
    return JsonResponse({"error": "Método no permitido"})
