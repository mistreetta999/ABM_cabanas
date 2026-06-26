""" Este archivo contiene las urls de la app registros."""
from django.urls import path

from . import views

APP_NAME = "registros"

urlpatterns = [
    path("", views.index, name="index"),
]
