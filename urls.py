""" archivo urls cabanas"""
from django.contrib import admin
from django.urls import path
from django_core import views
from django_core import views
from django.urls import path, include
urlpatterns = [
    path("admin/", admin.site.urls),
    path("pagina_principal/", views.pagina_principal, name="pagina_principal"),
    path("gestion/", views.gestion, name="gestion"),
  path("chatbot/", include("chatbot.urls", namespace="chatbot")),
]
