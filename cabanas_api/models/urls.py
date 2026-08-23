"""archivo de urls del proyecto django_local"""
from django.urls import include, path

app_name = "models"
urlpatterns = [
    # Administración Django

    # Punto de entrada de gestión
    path("gestion/", include("cabanas_apps.gestion_cabanas.urls")),

    # Interfaz principal
    path("interfaz/", include("django_core.cabanas_apps_django_interfaz_urls")),

    # Apps del sistema de cabañas
    path("cabanas/", include("cabanas_apps.cabanas.urls")),
    path("reservas/", include("cabanas_apps.reservas.urls")),
    path("alquileres/", include("cabanas_apps.alquileres.urls")),
    path("pagos/", include("cabanas_apps.pagos.urls")),
    path("registros/", include("cabanas_apps.registros.urls")),
    path("chatbot/", include("cabanas_apps.chatbot_app.urls")),
    path("clientes/", include("cabanas_apps.clientes.urls")),
]
