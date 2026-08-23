""" urls path"""
from django.contrib import admin
from django.urls import path, include
app_name = ["cabanas_principal"]
urlpatterns = [
    path("admin/", admin.site.urls),

    # Incluí tus aplicaciones aquí
    path("cabanas/", include("cabanas_apps.cabanas_app.urls")),
    path("usuarios/", include("cabanas_apps.usuarios.urls")),
    path("/clientes/", include("cabanas_apps.usuarios.urls")),
    path("/", include("cabanas_apps.usuarios.urls")),
    path("chatbot/", include("chatbot.urls")),
    path("alquileres/", include("cabanas_apps.alquileres.urls")),
    path("reservas/", include("cabanas_apps.reservas.urls")),
    path("pagos/", include("cabanas_apps.pagos.urls")),
    path("facturas/", include("cabanas_apps.facturas.urls")),
    path("", include("django_core.urls")),  # página principal
]
