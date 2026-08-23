""" Este archivo contiene la definición de los modelos para la aplicación de chatbot en Django."""
from django.db import models


class Message(models.Model):
    """Modelo que representa un mensaje en el chatbot."""
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.__class__.__name__


class Chatbot(models.Model):
    """ Modelo que representa un chatbot."""
    nombre = models.CharField(max_length=100, default="Chatbot Cabanas")
    descripcion = models.TextField(blank=True, null=True)

    
    def __str__(self):
        return self.__class__.__name__


class ChatbotHandler(models.Model):
    chatbot = models.ForeignKey(Chatbot, on_delete=models.CASCADE, related_name="handles")
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name="handles")
     
     
        
    def __str__(self):
        return self.__class__.__name__
