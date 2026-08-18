""" urls public"""
from django.urls import include, path

app_name = "public"

urlpatterns = [
    path("", include("cabanas_principal.urls")),
    path("reservas/", include("cabanas_apps.reservas.urls")),
    path("alquileres/", include("cabanas_apps.alquileres.urls")),
    path("clientes/", include("cabanas_apps.clientes.urls")),
    path("registros/", include("cabanas_apps.registros.urls")),
    path("cabanas/", include("cabanas_apps.cabanas.urls")),
    path("interfaz_gestion_cabanas/", include("django_core.cabanas_apps_django_interfaz_urls")),
    path("interfaz/", include("django_core.cabanas_apps_django_interfaz_urls")),
    path("pagos/", include("cabanas_apps.pagos.urls")),
    path("chatbot/", include("cabanas_apps.chatbot_app.urls")),
    
]
