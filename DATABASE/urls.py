"""URLs del sistema Cabanas: rutas Django y rutas HTML publicas."""
from django.urls import include, path

from cabanas_principal import handles as django_handles
from cabanas_principal import public_html


app_name = "cabanas_sistema"

urlpatterns = [
    # HTML publico
    path("", django_handles.pagina_principal, name="pagina_principal_django"),
    path("html/", public_html.index_html, name="html_index"),
    path("html/index.html", public_html.index_html, name="html_index_archivo"),
    path("html/pagina_principal.html", public_html.pagina_principal_html, name="html_pagina_principal"),

    # Django
    path("api/", include("cabanas_api.urls")),
    path("appconfig/", include("AppConfig.urls")),
    path("apps/", include("cabanas_apps.urls")),
    path("django_core/cabanas_apps_django/", include("django_core.cabanas_apps_django_urls", namespace="cabanas_apps_django_bridge")),
    path("django_core/cabanas_apps-django/", include("django_core.cabanas_apps_django_urls", namespace="cabanas_apps_django_bridge_guion")),
    path("django_core/cabanas_apps _django/", include("django_core.cabanas_apps_django_urls", namespace="cabanas_apps_django_bridge_espacio")),
    path("gestion/", include("cabanas_apps.gestion_cabanas.urls")),
    path("gestion_cabanas/", include("cabanas_apps.gestion_cabanas.urls", namespace="gestion_cabanas_alias")),
    path("getion_cabanas/", include("cabanas_apps.gestion_cabanas.urls", namespace="getion_cabanas_alias")),
    path("interfaz/", include("django_core.cabanas_apps_django_interfaz_urls")),
    path("interfaz_gestion_cabanas/", include("django_core.cabanas_apps_django_interfaz_urls", namespace="interfaz_gestion_cabanas_alias")),
    path("interfaz_getion_cabanas/", include("django_core.cabanas_apps_django_interfaz_urls", namespace="interfaz_getion_cabanas_alias")),
    path("inetrfaz_getion_cabanas/", include("django_core.cabanas_apps_django_interfaz_urls", namespace="inetrfaz_getion_cabanas_alias")),
    path("cabanas/", include("cabanas_apps.cabanas.urls")),
    path("cabanas_app/", include("cabanas_apps.cabanas_app.urls")),
    path("reservas/", include("cabanas_apps.reservas.urls")),
    path("alquileres/", include("cabanas_apps.alquileres.urls")),
    path("pagos/", include("cabanas_apps.pagos.urls")),
    path("registros/", include("cabanas_apps.registros.urls")),
    path("chatbot/", include("cabanas_apps.chatbot_app.urls")),
    path("clientes/", include("cabanas_apps.clientes.urls")),
]
