"""Rutas centrales de AppConfig."""
from django.urls import include, path

from . import handles

app_name = ["appconfig"]

urlpatterns = [

    path('', handles.lista_cabanas, name='lista_cabanas'),
    path('<int:cabana_id>/', handles.detalle_cabana, name='detalle_cabana'),
    path('crear/', handles.crear_cabana, name='crear_cabana'),
    path('editar/<int:cabana_id>/', handles.editar_cabana, name='editar_cabana'),
    path('eliminar/<int:cabana_id>/', handles.eliminar_cabana, name='eliminar_cabana'),
    path('api/', handles.api_cabanas, name='api_cabanas'),


    path("django_core/", include("django_core.urls")),
    path("chatbot/", include("cabanas_apps.chatbot_app.urls")),
    path("", handles.appconfig_home, name="home"),
    path("rutas/", handles.rutas_disponibles, name="rutas_disponibles"),
    path("api/", include("cabanas_api.urls")),
    path("apps/", include("cabanas_apps.urls")),
    path("django/", include("django_core.urls")),
    path("django-local/", include("django_local.urls")),
    path("templates/", include("Templates.urls")),
    path("gestion_cabanas/", include("cabanas_apps.gestion_cabanas.urls")),
    path("interfaz_gestion_cabanas/", include("django_core.cabanas_apps_django_interfaz_urls")),
    path("cabanas/", include("cabanas_apps.cabanas.urls")),
    path("cabanas-app/", include("cabanas_apps.cabanas_app.urls")),
    path("cabanas_app/", include("cabanas_apps.cabanas_app.urls")),
    path("reservas/", include("cabanas_apps.reservas.urls")),
    path("alquileres/", include("cabanas_apps.alquileres.urls")),
    path("clientes/", include("cabanas_apps.clientes.urls")),
    path("registros/", include("cabanas_apps.registros.urls")),
    path("pagos/", include("cabanas_apps.pagos.urls")),
    path("chatbot/", include("cabanas_apps.chatbot_app.urls")),
    path("usuarios/", include("cabanas_apps.usuarios_sistema.urls")),
    path("web/", include("web.urls")),
]
