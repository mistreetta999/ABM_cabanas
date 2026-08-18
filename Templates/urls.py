"""URLs para agrupar las vistas que usan templates del sistema."""
from django.urls import include, path

app_name = "templates"

urlpatterns = [
    path("gestion/", include("cabanas_apps.gestion_cabanas.urls")),
    path("interfaz/", include("django_core.cabanas_apps_django_interfaz_urls")),
    path("cabanas/", include("cabanas_apps.cabanas.urls")),
    path("reservas/", include("cabanas_apps.reservas.urls")),
    path("alquileres/", include("cabanas_apps.alquileres.urls")),
    path("pagos/", include("cabanas_apps.pagos.urls")),
    path("registros/", include("cabanas_apps.registros.urls")),
    path("chatbot/", include("cabanas_apps.chatbot_app.urls")),
    path("clientes/", include("cabanas_apps.clientes.urls")),
]
