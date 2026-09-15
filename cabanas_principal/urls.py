"""URLs principales del proyecto cabanas_principal"""

from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from django_core.cabanas_apps_django.reservas.views import ReservaViewSet

try:
    from django_core.cabanas_apps_django.cabanas.views import CabanaViewSet
except ImportError:  # pragma: no cover

    class CabanaViewSet:  # type: ignore[no-redef]
        """Fallback para evitar errores de importación en análisis estático."""


try:
    from django_core.cabanas_apps_django.alquileres.views import AlquilerViewSet
except ImportError:  # pragma: no cover

    class AlquilerViewSet:  # type: ignore[no-redef]
        """Fallback para evitar errores de importación en análisis estático."""


try:
    from django_core.cabanas_apps_django.facturas.views import FacturaViewSet
except ImportError:  # pragma: no cover

    class FacturaViewSet:  # type: ignore[no-redef]
        """Fallback para evitar errores de importación en análisis estático."""


# Router principal
router = DefaultRouter()
router.register(r"reservas", ReservaViewSet)
router.register(r"cabanas", CabanaViewSet)
router.register(r"alquileres", AlquilerViewSet)
router.register(r"facturas", FacturaViewSet)


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
    path(
        "pagina_principal.html",
        TemplateView.as_view(template_name="pagina_principal.html"),
        name="pagina_principal_html_sin_barra",
    ),
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
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),  # todas las rutas de la API REST
    path("reservas/", include("django_core.cabanas_apps_django.reservas.urls")),
    path("clientes/", include("django_core.cabanas_apps_django.clientes.urls")),
    path("cabanas/", include("django_core.cabanas_apps_django.cabanas.urls")),
    path("alquileres/", include("django_core.cabanas_apps_django.alquileres.urls")),
    path("facturas/", include("django_core.cabanas_apps_django.facturas.urls")),
]
