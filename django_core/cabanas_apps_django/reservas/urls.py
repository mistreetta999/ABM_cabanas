"""Este archivo contiene las urls de la app reservas.
"""
from django.urls import path
from . import views

app_name = "reservas"

urlpatterns = [
    path("lista/", views.lista_reservas, name="lista_reservas"),
]
