""" Este archivo contiene las urls de la app cabanas."""
from django.urls import path
from django.urls import include

from cabanas_apps.cabanas import views
from . import views
APP_NAME = "cabanas"

urlpatterns = [
    path("", views.index, name="index"),
    path("lista/", views.lista_cabanas, name="lista_cabanas"),
    path('',include('cabanas_api.urls')),
    path('', include('cabanas_api.urls')),  # o cabanas_aps
]
