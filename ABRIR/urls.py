"""Puente de URLs para la app ABRIR"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from DATABASE.views import (
    PagoDeleteView,
    PagoDetailView,
    PagoCreateView,
    PagoListView,
    PagoUpdateView,
)

urlpatterns = [
    path("admin/", admin.site.urls),

    # Apps principales
    path("clientes/", include("clientes.urls")),
    path("reservas/", include("reservas.urls")),
    path("alquileres/", include("alquileres.urls")),
    path("cabanas/", include("cabanas.urls")),
    path("facturas/", include("facturas.urls")),

    # Página principal
    path("", include("html_local.urls")),
    path(
        "pagina_principal.html",
        TemplateView.as_view(template_name="pagina_principal.html"),
        name="pagina_principal_html_sin_barra",
    ),

    # Pagos
    path("pagos/", PagoListView.as_view(), name="lista_pagos"),
    path("pagos/<int:pk>/", PagoDetailView.as_view(), name="detalle_pago"),
    path("pagos/nuevo/", PagoCreateView.as_view(), name="crear_pago"),
    path("pagos/<int:pk>/editar/", PagoUpdateView.as_view(), name="editar_pago"),
    path("pagos/<int:pk>/borrar/", PagoDeleteView.as_view(), name="borrar_pago"),
]
