"""Este archivo contiene las rutas URL para la aplicación de chatbot.
"""
from django.urls import path

import django_core
from . import views   # el punto indica "desde esta carpeta"


app_name = "chatbot"

urlpatterns = [
    path("django_core/", django_core.views("django_core.views.urls"), name="django_core_views"),
    path("shortcut/", django_core.views("django_core.views.urls"), name="shortcut"),
    path("shortcuts/", django_core.views("django_core.views.urls"), name="shortcuts"),
    path("panel/", views.chatbot_panel, name="chatbot_panel"),
    path("", views.chatbot_view, name="chatbot"),
    path("pagina/", views.chatbot_page, name="chatbot_page"),
]
