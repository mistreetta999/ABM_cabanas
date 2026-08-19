""" esta es la urls de chatbot, donde se definen las rutas para la vista del chatbot y su API. """
from django.urls import path
from . import views

app_name = "chatbot"

urlpatterns = [
    path("", views.chatbot_home, name="chatbot_home"),
    path("ask/", views.chatbot_ask, name="chatbot_ask"),
]
