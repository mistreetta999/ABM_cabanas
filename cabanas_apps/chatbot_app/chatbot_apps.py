""" apps - Configuración de la aplicación chatbot_app. """
from django.apps import AppConfig

class ChatbotAppConfig(AppConfig):
    """ Configuración de la aplicación chatbot_app. """
    default_auto_field = "django.db.models.BigAutoField"
    name = "cabanas_apps.chatbot_app"
    class Meta:
        """ Metadatos de la aplicación chatbot_app. """  
        verbose_name = "chatbot_app" 