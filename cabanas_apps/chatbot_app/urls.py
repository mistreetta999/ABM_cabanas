"""Este archivo contiene las rutas URL para la aplicación de chatbot.
"""
from django.urls import path
from . import views

urlpatterns = [
    path("api/", views.chatbot_api, name="chatbot_api"),
    path("", views.chatbot_home, name="chatbot_home"),
    
]
