""" views chatbot"""
import json
from django.http import JsonResponse, HttpResponse, HttpRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .chatbot import ChatBot

bot = ChatBot()

class chatbot_home:
    """ views chatbot"""
    @csrf_exempt
    def chatbot_home(self, request: HttpRequest) -> JsonResponse:
        """ Maneja las solicitudes POST al endpoint del chatbot y devuelve respuestas basadas en el mensaje recibido."""
        if request.method != 'POST':
            return JsonResponse({'reply': 'Envia una consulta para recibir informacion.'})

        data = json.loads(request.body or '{}')
        message = data.get('message', '').lower()
        if 'precio' in message or 'tarifa' in message:
            reply = 'Las tarifas dependen de la cantidad de huespedes y fechas. Podes dejar tus datos en reservas.'
        elif 'ubicacion' in message or 'donde' in message:
            reply = 'Estamos en Mina Clavero, Cordoba, cerca del centro y de los balnearios principales.'
        else:
            reply = 'Gracias por consultar. Para reservar, comunicate por WhatsApp o carga una reserva en el ABM.'
        return JsonResponse({'reply': reply})

class ChatBotRespuestaViews:
    """ views chatbot"""
    def chatbot(self, request: HttpRequest) -> JsonResponse:
        """ Maneja las solicitudes POST al endpoint del chatbot y devuelve respuestas basadas en el mensaje recibido."""
        if request.method != 'POST':
            return JsonResponse({'reply': 'Envia una consulta para recibir informacion.'})

        data = json.loads(request.body or '{}')
        message = data.get('message', '').lower()
        if 'precio' in message or 'tarifa' in message:
            reply = 'Las tarifas dependen de la cantidad de huespedes y fechas. Podes dejar tus datos en reservas.'
        elif 'ubicacion' in message or 'donde' in message:
            reply = 'Estamos en Mina Clavero, Cordoba, cerca del centro y de los balnearios principales.'
        else:
            reply = 'Gracias por consultar. Para reservar, comunicate por WhatsApp o carga una reserva en el ABM.'
        return JsonResponse({'reply': reply})
class Chatbotviews:
    """ views chatbot"""
    def index(self, request: HttpRequest) -> HttpResponse:
        """ index chatbot"""
        return render(request, 'chatbot/index.html')
class ChatbotViewsTemplates:
    """ views chatbot"""
    def index(self, request: HttpRequest) -> HttpResponse:
        """ index chatbot"""
        return render(request, 'chatbot/index.html')    

def chatbot_page(request: HttpRequest) -> HttpResponse:
    """Renderiza la página del chatbot."""
    return render(request, 'chatbot/chatbot.html')


@csrf_exempt    
def chatbot_api(request: HttpRequest) -> JsonResponse:
    """ Maneja las solicitudes POST al endpoint del chatbot y devuelve respuestas basadas en el mensaje recibido."""
    if request.method != 'POST':
        return JsonResponse({'reply': 'Envia una consulta para recibir informacion.'})

    data = json.loads(request.body or '{}')
    message = data.get('message', '').lower()
    if 'precio' in message or 'tarifa' in message:
        reply = 'Las tarifas dependen de la cantidad de huespedes y fechas. Podes dejar tus datos en reservas.'
    elif 'ubicacion' in message or 'donde' in message:
        reply = 'Estamos en Mina Clavero, Cordoba, cerca del centro y de los balnearios principales.'
    else:
        reply = 'Gracias por consultar. Para reservar, comunicate por WhatsApp o carga una reserva en el ABM.'
    return JsonResponse({'reply': reply})
def index(request):
    """index chatbot"""
    return render(request, "chatbot/index.html")
class ChatbotPanel:
    """ views chatbot"""
    def chatbot_panel(self, request: HttpRequest) -> HttpResponse:
        """Renderiza la página del panel del chatbot."""
        if request.method == "POST":
            user_message = request.POST.get("message", "")
            response = bot.respond(user_message)
            return render(request, "chatbot/panel.html", {"response": response})
        return render(request, "chatbot/panel.html", {"response": bot.welcome_message})
