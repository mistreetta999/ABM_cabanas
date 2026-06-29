"""Este archivo contiene las rutas URL para la aplicación de chatbot.
"""
from django.urls import path
from . import views   # el punto indica "desde esta carpeta"


APP_NAME = "chatbot"


urlpatterns = [
    path("", views.chatbot_panel, name="chatbot_panel"),
    path('', views.chatbot_page, name='chatbot_page'),
path("chatbot/", include("chatbot_app.urls")),

]
