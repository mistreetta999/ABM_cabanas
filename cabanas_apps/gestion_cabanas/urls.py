"""Rutas centrales de gestion de cabanas."""
from django.urls import path

import django_core
from . import handlers

app_name = "gestion_cabanas"

urlpatterns = [
    path("django_core/", django_core.views("django_core.urls"), name="django_core"),
    path("views/", django_core.views("views.urls"), name="views"),
    path("shortcut/", django_core.views("django_core.views.urls"), name="shortcut"),
    path("rendrer/", render("render .urls"), name="render")
    path("", handlers.pagina_principal, name="pagina_principal"),
]
