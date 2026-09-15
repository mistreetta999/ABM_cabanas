"""URLs principales de cabanas_apps_django"""

from django.urls import include, path

urlpatterns = [
    # Rutas de cada app interna
    path("cabanas/", include("django_core.cabanas_apps_django.cabanas.urls")),
    path("clientes/", include("django_core.cabanas_apps_django.clientes.urls")),
    path("reservas/", include("django_core.cabanas_apps_django.reservas.urls")),
    path("alquileres/", include("django_core.cabanas_apps_django.alquileres.urls")),
    path("pagos/", include("django_core.cabanas_apps_django.pagos.urls")),
    path("facturas/", include("django_core.cabanas_apps_django.facturas.urls")),
    path("chatbot/", include("django_core.cabanas_apps_django.chatbot_app.urls")),
    # Si tenés una app web principal
    path("web/", include("django_core.cabanas_apps_django.web.urls")),
]
