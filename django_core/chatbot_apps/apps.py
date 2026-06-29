""" chatbot_apps configuration """
from django.apps import AppConfig

class ChatbotAppConfig(AppConfig):
    """ Configuration for the chatbot_apps application. """
    default_auto_field = "django.db.models.BigAutoField"
    name = "cabanas_apps.chatbot_app"
    class Meta:
        """ Metadata for the chatbot_apps application. """
        verbose_name = "chatbot_apps"
      app_label = "chatbot_app"
