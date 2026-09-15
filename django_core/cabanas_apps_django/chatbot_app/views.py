"""views chatbot"""

import json

from django.db import models
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt

import cabanas_principal


class Chatbot(View):
    """Vista principal del chatbot."""

    @csrf_exempt
    def chatbot_home(self, request: HttpRequest) -> JsonResponse:
        """respuestas basadas en el mensaje recibido."""
        if request.method != "POST":
            return JsonResponse(
                {"reply": "Envia una consulta para recibir informacion."}
            )

        data = json.loads(request.body or "{}")
        message = data.get("message", "").lower()
        if "precio" in message or "tarifa" in message:
            reply = "Las tarifas dependen de la cantidad de huespedes y fechas. Podes dejar tus datos en reservas."
        elif "ubicacion" in message or "donde" in message:
            reply = "Estamos en Mina Clavero, Cordoba, cerca del centro y de los balnearios principales."
        else:
            reply = "Gracias por consultar. Para reservar, comunicate por WhatsApp o carga una reserva en el ABM."
        return JsonResponse({"reply": reply})


class ChatBotRespuestaViews:
    """views chatbot"""

    def chatbot(self, request: HttpRequest) -> JsonResponse:
        """Maneja las solicitudes POST al endpoint del chatbot y devuelve respuestas basadas en el mensaje recibido."""
        if request.method != "POST":
            return JsonResponse(
                {"reply": "Envia una consulta para recibir informacion."}
            )

        data = json.loads(request.body or "{}")
        message = data.get("message", "").lower()
        if "precio" in message or "tarifa" in message:
            reply = "Las tarifas dependen de la cantidad de huespedes y fechas. Podes dejar tus datos en reservas."
        elif "ubicacion" in message or "donde" in message:
            reply = "Estamos en Mina Clavero, Cordoba, cerca del centro y de los balnearios principales."
        else:
            reply = "Gracias por consultar. Para reservar, comunicate por WhatsApp o carga una reserva en el ABM."
        return JsonResponse({"reply": reply})


class Chatbotviews:
    """views chatbot"""

    def index(self, request: HttpRequest) -> HttpResponse:
        """index chatbot"""
        return render(request, "chatbot/index.html")


class ChatbotViewsTemplates:
    """views chatbot"""

    def index(self, request: HttpRequest) -> HttpResponse:
        """index chatbot"""
        return render(request, "chatbot/index.html")


class ChatbotHomeView(View):
    """Vista principal del chatbot."""

    def get(self, request: HttpRequest) -> HttpResponse:
        """Renderiza la página principal del chatbot."""
        return render(request, "chatbot/index.html")


def chatbot_page(request: HttpRequest) -> HttpResponse:
    """Renderiza la página del chatbot."""
    return render(request, "chatbot/chatbot.html")


class ChatbotInteractView(View):
    """Vista para la interacción con el chatbot."""

    @csrf_exempt
    def post(self, request: HttpRequest) -> JsonResponse:
        """Maneja las solicitudes POST al endpoint del chatbot y devuelve respuestas basadas en el mensaje recibido."""
        data = json.loads(request.body or "{}")
        user_message = data.get("message", "")
        reply = _respond(user_message)
        return JsonResponse({"reply": reply})


class Message(models.Model):
    """Mensaje del chat."""

    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    sender = models.CharField(
        max_length=50, choices=[("cliente", "Cliente"), ("chatbot", "Chatbot")]
    )
    chatbot = models.CharField(
        max_length=50, choices=[("cliente", "Cliente"), ("chatbot", "Chatbot")]
    )

    class Meta:
        """Metadatos del modelo Message."""

        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.sender}"


def _respond(message: str) -> str:
    """Genera una respuesta para el mensaje recibido."""
    message = (message or "").lower()
    if "precio" in message or "tarifa" in message:
        return "Las tarifas dependen de la cantidad de huespedes y fechas. Podes dejar tus datos en reservas."
    if "ubicacion" in message or "donde" in message:
        return "Estamos en Mina Clavero, Cordoba, cerca del centro y de los balnearios principales."
    return "Gracias por consultar. Para reservar, comunicate por WhatsApp o carga una reserva en el ABM."


class ChatbotHistoryView(View):
    """Vista para mostrar el historial de conversaciones con el chatbot."""

    def get(self, _request: HttpRequest) -> HttpResponse:
        """ "get"""
        return HttpResponse("preguntar")


def chatbot_panel(request: HttpRequest) -> HttpResponse:
    """Panel HTML del chatbot."""
    if request.method == "POST":
        user_message = request.POST.get("message", "")
        response = _respond(user_message)
        return render(request, "chatbot/panel.html", {"response": response})

    welcome = "Bienvenido al chatbot."
    return render(request, "chatbot/panel.html", {"response": welcome})


def chatbot_view(request: HttpRequest) -> HttpResponse:
    """Interfaz principal del chatbot."""
    return render(request, "chatbot/chatbot.html")


def index(request: HttpRequest) -> HttpResponse:
    """Página de inicio del chatbot."""
    return render(request, "chatbot/index.html")
