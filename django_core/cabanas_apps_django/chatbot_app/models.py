""" Modelos de la aplicación Chatbot. """
from django.db import models
from ..clientes.models import Cliente
class Chatbot(models.Model):
    """
    Representa el chatbot dentro de la aplicación.
    """
    nombre = models.CharField(max_length=100, default="Chatbot Cabanas")
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return str(self.nombre)
    class Meta:
        """ Metadatos del modelo Chatbot """
        verbose_name = "Chatbot"
        verbose_name_plural = "Chatbots"
        ordering = ["nombre"]

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
        """ Metadatos del modelo Message """
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.sender}"



class ChatbotHandler(models.Model):
    """
    Relación entre el chatbot y los mensajes.
    """
    chatbot = models.ForeignKey(Chatbot, on_delete=models.CASCADE, related_name="handles")
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name="handles")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="chatbot_messages", null=True, blank=True)

    def __str__(self):
        return f"{self.chatbot} - {self.message}"
