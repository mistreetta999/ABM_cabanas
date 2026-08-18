"""URLs agregadas de cabanas_apps."""
from django.http import HttpRequest
from django.urls import include, path

import django_core
from cabanas_apps.interfaz_gestion_cabanas.handles import render_unified_panel

app_name = "cabanas_apps"

DJANGO_CORE_VIEWS = "django_core.views.urls"


def pagina_principal(request: HttpRequest)->HttpResponse:
    """Panel compartido para las apps del sistema."""
    return render_unified_panel(
        request,
        "Panel Apps",
        "Apps, templates y web gestionados desde Python.",
    )


urlpatterns = [
    path("django_core/", django_core.views(DJANGO_CORE_VIEWS), name="django_core_views"),
    path("shortcut/", django_core.views(DJANGO_CORE_VIEWS), name="shortcut"),
    path("shortcuts/", django_core.views(DJANGO_CORE_VIEWS), name="shortcuts"),
    path("", pagina_principal, name="pagina_principal"),
    path("reservas/", include("cabanas_apps.reservas.urls")),
    path("alquileres/", include("cabanas_apps.alquileres.urls")),
    path("clientes/", include("cabanas_apps.clientes.urls")),
    path("registros/", include("cabanas_apps.registros.urls")),
    path("cabanas/", include("cabanas_apps.cabanas.urls")),
    path("gestion/", include("cabanas_apps.gestion_cabanas.urls")),
    path("interfaz_gestion_cabanas/", include("django_core.cabanas_apps_django_interfaz_urls")),
    path("pagos/", include("cabanas_apps.pagos.urls")),
    path("facturas/", include("cabanas_apps.facturas.urls")),
    path("chatbot/", include("cabanas_apps.chatbot_app.urls")),
# REMOVED usuarios_sistema
    path("cabanas_app/", include("cabanas_apps.cabanas_app.urls")),
]
