""" models de cabanas"""
from django.db import models
from django.db import models
from cabanas_apps.clientes.models import Cliente
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db.models import Sum
from pathlib import Path


class ChatbotResponse(models.Model):
    """
    Respuestas del chatbot a los mensajes del cliente.
    """
    chatbot = models.ForeignKey("Chatbot", on_delete=models.CASCADE, related_name="responses")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ Metadatos del modelo ChatbotResponse """
        verbose_name = "Chatbot Response"
        verbose_name_plural = "Chatbot Responses"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Response from {self.chatbot} at {self.created_at}"

class Message(models.Model):
    """
    Mensajes enviados por el cliente o el chatbot.
    """
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    sender = models.CharField(max_length=50, choices=[("cliente", "Cliente"), ("chatbot", "Chatbot")])

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.sender}"


class Chatbot(models.Model):
    """
    Representa el chatbot dentro de la aplicación.
    """
    nombre = models.CharField(max_length=100, default="Chatbot Cabanas")
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self:models.Model) -> str:
        return str(self.nombre)


class ChatbotHandler(models.Model):
    """
    Relación entre el chatbot y los mensajes.
    """
    chatbot = models.ForeignKey(Chatbot, on_delete=models.CASCADE, related_name="handles")
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name="handles")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="chatbot_messages", null=True, blank=True)

    def __str__(self):
        return f"{self.chatbot} - {self.message}"

class Cabana(models.Model):
    """class cabana"""
    nombre = models.CharField(max_length=100, unique=True)
    capacidad = models.PositiveIntegerField()
    descripcion = models.TextField(blank=True, null=True)
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)

    class Meta:
        """class meta"""
        verbose_name = "Cabaña"
        verbose_name_plural = "Cabañas"

    def __str__(self) -> str:
        return str(self.nombre)


class Cliente(models.Model):
    """ class cliente"""
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        """class meta"""
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ["apellido"]

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Reserva(models.Model):
    """class reserva"""
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="reservas")
    cabana = models.ForeignKey(Cabana, on_delete=models.CASCADE, related_name="reservas")
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    cantidad_personas = models.PositiveIntegerField(default=1)
    pagada = models.BooleanField(default=False)

    class Meta:
        """class meta"""
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
        ordering = ["fecha_inicio"]

    def __str__(self):
        return f"Reserva de {self.cliente} en {self.cabana}"
