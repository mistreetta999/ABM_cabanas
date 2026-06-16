import json
from datetime import datetime, timedelta
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Reserva
from chatbot.chatbot import 

class Chatbot:
    def __init__(self):
        self.mensajes = self.mensajes
        self.buscar = self.buscar
        self.pedir = self.pedir
        self.respuestas = self.respuestas

class Chatbot:
    def __init__(self):
        self.mensajes = self.mensajes
        self.buscar = self.buscar
        self.pedir = self.pedir
        self.respuestas = self.respuestas
        self.db = self.db
         

    def obtener_respuesta(self, mensaje):
        self.respuestas = {
            "hola": "¡Hola! ¿En qué puedo ayudarte?",
            "adiós": "¡Hasta luego! Que tengas un buen dia ",
            "gracias": "De nada, para lo que necesites aquí estoy",
        }

        return self.respuestas.get(mensaje, "No entendí tu consulta, ¿puedes repetirla?")

@csrf_exempt
def chatbot_api(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message", "").lower()
        reply = "No entendí tu consulta, ¿puedes repetirla?"

        hoy = datetime.today().date()

        # Día
        if "día" in user_message or "hoy" in user_message:
            reservas = Reserva.objects.filter(fecha_inicio__lte=hoy, fecha_fin__gte=hoy)
            reply = f"Reservas para hoy: {'Sí' if reservas.exists() else 'No'}"

        # Semana
        elif "semana" in user_message:
            inicio = hoy
            fin = hoy + timedelta(days=7)
            reservas = Reserva.objects.filter(fecha_inicio__lte=fin, fecha_fin__gte=inicio)
            reply = f"Reservas esta semana: {'Sí' if reservas.exists() else 'No'}"

        # Mes
        elif "mes" in user_message:
            inicio_mes = hoy.replace(day=1)
            if hoy.month == 12:
                fin_mes = hoy.replace(year=hoy.year+1, month=1, day=1) - timedelta(days=1)
            else:
                fin_mes = hoy.replace(month=hoy.month+1, day=1) - timedelta(days=1)
            reservas = Reserva.objects.filter(fecha_inicio__lte=fin_mes, fecha_fin__gte=inicio_mes)
            reply = f"Reservas este mes: {'Sí' if reservas.exists() else 'No'}"

        return JsonResponse({"reply": reply})
