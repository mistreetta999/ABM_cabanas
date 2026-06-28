""" Este archivo contiene las urls de la app alquileres."""
from django.urls import path
from . import views

APP_NAME = "reservas_alquileres"

urlpatterns = [
    path("reservas/", views.reservas_list, name="reservas_list"),
    path("alquileres/", views.alquileres_list, name="alquileres_list"),
]
