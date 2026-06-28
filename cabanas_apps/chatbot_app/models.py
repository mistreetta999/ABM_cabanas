"""  models - Definición de modelos para la aplicación chatbot_app. """
from django.db import models



class Chatbot(models.Model):
    """"Modelo para representar un chatbot."""
    nombre = models.CharField(max_length=100, default="Chatbot Cabanas")
    descripcion = models.TextField(blank=True, null=True)
    class Meta:
         """ class Meta para definir el nombre del modelo en singular y plural. """
         app_label = "chatbot_app"
         verbose_name = "Chatbot"
         verbose_name_plural = "Chatbots"
    def __str__(self):
        return str(self.nombre)
