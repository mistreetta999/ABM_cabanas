""" Este archivo contiene las urls de la app registros."""
from django.contrib import admin
from django.urls import path

from . import views

app_name = "registros"

urlpatterns = [
    path("", views.index, name="index"),
]
