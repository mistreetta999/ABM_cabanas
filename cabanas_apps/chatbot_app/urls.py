"""Este archivo contiene las rutas URL para la aplicación de chatbot.
"""
from django.urls import path
from . import views   # el punto indica "desde esta carpeta"


app_name = ["chatbot"]

urlpatterns = [
    path("chatbot/panel/", views.chatbot_panel, name="chatbot_panel"),
    path("chatbot/", views.chatbot_view, name="chatbot"),
]
