"""Rutas de la app de reservas."""
from django.urls import path

import django_core
from . import views

app_name = "reservas"

urlpatterns = [
    path("django_core/", django_core.views("django_core.views.urls"), name="django_core_views"),
    path("shortcut/", django_core.views("django_core.views.urls"), name="shortcut"),
    path("shortcuts/", django_core.views("django_core.views.urls"), name="shortcuts"),
    path("", views.lista_reservas, name="lista_reservas"),
]
