"""URLs para la aplicación de Chatbot en el sistema de cabañas."""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("chatbot/", views.chatbot_view, name="chatbot_view"),
    path("chatbot/panel/", views.chatbot_panel, name="chatbot_panel"),
    path("chatbot/api/", views.chatbot_api, name="chatbot_api"),
]
