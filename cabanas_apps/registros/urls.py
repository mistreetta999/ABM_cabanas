"""URL configuration for cabanas_apps.registros app."""
from django.urls import path
from . import views


app_name = "registros"  # pylint: disable=invalid-name

urlpatterns = [
    path("actividades/", views.lista_actividades, name="lista_actividades"),
]
