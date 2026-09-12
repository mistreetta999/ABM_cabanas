"""URLs para agrupar las vistas que usan templates del sistema."""
from django.urls import include, path

app_name = "templates"

urlpatterns = [
    #    path("interfaz/", include("django_core.cabanas_apps_django.interfaz_gestion_cabanas.urls")),
    path("cabanas/", include("django_core.cabanas_apps_django.cabanas.urls")),
    path("reservas/", include("django_core.cabanas_apps_django.reservas.urls")),
    path("alquileres/", include("django_core.cabanas_apps_django.alquileres.urls")),
    path("pagos/", include("django_core.cabanas_apps_django.pagos.urls")),
    path("registros/", include("django_core.cabanas_apps_django.registros.urls")),
    path("chatbot/", include("cabanas_apps.chatbot_app.urls")),
    path("clientes/", include("cabanas_apps.clientes.urls")),
]
