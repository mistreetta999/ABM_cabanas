"""Archivo de urls para la app alquileres"""
from django.urls import path
from django_core.cabanas_apps_django.alquileres.views import AlquilerListView

from .views import (
    AlquilerListView,
    AlquilerCreateView,
    AlquilerUpdateView,
    AlquilerDeleteView,
)


app_name = "alquileres"

urlpatterns = [
    path("alquileres/", AlquilerListView.as_view(), name="alquileres_list"),
    path("alquileres", AlquilerListView.as_view(), name="alquiler_list"),
    path("nuevo/", AlquilerCreateView.as_view(), name="alquiler_create"),
    path("<int:pk>/editar/", AlquilerUpdateView.as_view(), name="alquiler_update"),
    path("<int:pk>/guardar/", AlquilerUpdateView.as_view(), name="alquiler_guardar"),
    path("<int:pk>/imprimir/", AlquilerUpdateView.as_view(), name="imprimir"),
    path("<int:pk>/borrar/", AlquilerDeleteView.as_view(), name="alquiler_delete"),
]

