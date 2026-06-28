"""Este archivo contiene las rutas URL para la aplicación de chatbot.
"""
from django.urls import path
from .views import chatbot_page, chatbot_api
from django.views import Views
from django.urls import include
APP_NAME = "chatbot"

urlpatterns = [
     path("", views.index, name="index"),
    path('', chatbot_page, name='chatbot_page'),
    path('api/', chatbot_api, name='chatbot_api'),
    path("chatbot/", include("chatbot.urls", namespace="chatbot")),

]
