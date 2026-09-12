"""URLs principales del proyecto cabanas_principal"""

from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path


def lista_cabanas(request):
    """Devuelve la lista de cabañas."""
    _ = request.method
    return HttpResponse("Lista de cabañas")


def lista_reservas(request):
    """Devuelve la lista de reservas."""
    _ = request.method
    return HttpResponse("Lista de reservas")


def vista_pagos(request):
    """Devuelve la vista de pagos."""
    _ = request.method
    return HttpResponse("Vista de pagos")


urlpatterns = [
    path("cabanas/", lista_cabanas, name="lista_cabanas"),
    path("reservas/", lista_reservas, name="lista_reservas"),
    path("pagos/", vista_pagos, name="vista_pagos"),
    path("admin/", admin.site.urls),

    # Apps internas
    path("cabanas/", include("django_core.cabanas_apps_django.cabanas.urls")),
    path("clientes/", include("django_core.cabanas_apps_django.clientes.urls")),
    path("reservas/", include("django_core.cabanas_apps_django.reservas.urls")),
    path("pagos/", include("django_core.cabanas_apps_django.pagos.urls")),
    path("web/", include("django_core.cabanas_apps_django.web.urls")),
    path("chatbot/", include("django_core.cabanas_apps_django.chatbot_app.urls")),
    path("alquileres/", include("django_core.cabanas_apps_django.alquileres.urls")),
    path("facturas/", include("django_core.cabanas_apps_django.facturas.urls")),
    # API de alquileres
    path("api/", include("cabanas_api.urls")),
]
