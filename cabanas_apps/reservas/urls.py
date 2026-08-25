"""Rutas de la app de reservas."""
from django.urls import path

import django_core
from . import views

app_name = "reservas"

urlpatterns = [
    # Rutas mínimas para evitar dependencias a módulos inexistentes
    path("", views.lista_reservas, name="lista_reservas"),
]
