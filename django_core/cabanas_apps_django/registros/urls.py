"""URL configuration for cabanas_apps.registros app."""
from django.urls import path
from . import views


app_name = "registros"  # pylint: disable=invalid-name

urlpatterns = [
    path("actividades/", views.ActividadCabanasListView.as_view(), name="lista_actividades"),
]
