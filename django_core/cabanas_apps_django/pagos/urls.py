"""URLs de la aplicación Pagos, integradas con el sistema."""

from django.urls import path, include
from .views import (
    PagoListView,
    PagoCreateView,
    PagoUpdateView,
    PagoDeleteView,
    PagoDetailView,
)

# pylint: disable=invalid-name
app_name = "pagos"

urlpatterns = [
    path("", PagoListView.as_view(), name="lista_pagos"),
    path("<int:pk>/", PagoDetailView.as_view(), name="detalle_pago"),
    path("crear/", PagoCreateView.as_view(), name="crear_pago"),
    path("<int:pk>/editar/", PagoUpdateView.as_view(), name="editar_pago"),
    path("<int:pk>/eliminar/", PagoDeleteView.as_view(), name="eliminar_pago"),
    path("alquileres/", include("django_core.cabanas_apps_django.alquileres.urls")),

    # 🔗 Integraciones con otras apps del sistema
    path("cabanas/", include("cabanas.urls")),
    path("clientes/", include("clientes.urls")),
    path("facturas/", include("facturas.urls")),
    path("usuarios/", include("usuarios.urls")),
    path("chatbot/", include("chatbot_app.urls")),
    path("gestion/", include("gestion_cabanas.urls")),
    path("interfaz/", include("interfaz_gestion_cabanas.urls")),
]
