"""URL configuration for cabanas_apps project."""
from django.urls import path
from . import views

APP_NAME = "clientes"

urlpatterns = [
    path("lista/", views.lista_clientes, name="lista_clientes"),

]
