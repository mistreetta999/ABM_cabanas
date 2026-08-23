"""URLs Django relacionadas con las apps del sistema."""
from django.urls import include, path

import django_core

app_name = "django_core"

urlpatterns = [
    path("shortcut/", django_core.views("django_core.views.urls"), name="shortcut"),
    path("shortcuts/", django_core.views("django_core.views.urls"), name="shortcuts"),
    path("render/", include("django_core.render_support.urls")),
    path("api/", include("cabanas_api.urls")),
    path("apps/", include("cabanas_apps.urls")),
    path("django_local/", include("django_local.urls")),
    path("templates/", include("Templates.urls")),
    path("gestion/", include("cabanas_apps.gestion_cabanas.urls")),
    path("gestion_cabanas/", include("cabanas_apps.gestion_cabanas.urls")),
    path("interfaz_gestion_cabanas/", include("django_core.cabanas_apps_django_interfaz_urls")),
    path("cabanas/", include("cabanas_apps.cabanas.urls")),
    path("cabanas-app/", include("cabanas_apps.cabanas_app.urls")),
    path("cabanas_app/", include("cabanas_apps.cabanas_app.urls")),
    path("reservas/", include("cabanas_apps.reservas.urls")),
    path("alquileres/", include("cabanas_apps.alquileres.urls")),
    path("pagos/", include("cabanas_apps.pagos.urls")),
    path("facturas/", include("cabanas_apps.facturas.urls")),
    path("registros/", include("cabanas_apps.registros.urls")),
    path("chatbot/", include("cabanas_apps.chatbot_app.urls")),
    path("clientes/", include("cabanas_apps.clientes.urls")),
    path("web/", include("web.urls")),
]
