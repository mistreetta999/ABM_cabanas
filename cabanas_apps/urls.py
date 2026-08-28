"""URLs principales de la carpeta cabanas_apps."""

from django.urls import path, include

urlpatterns = [
    # Apps principales del sistema
    path("cabanas/", include("cabanas.urls")),
    path("alquileres/", include("alquileres.urls")),
    path("reservas/", include("reservas.urls")),
    path("clientes/", include("clientes.urls")),
    path("facturas/", include("facturas.urls")),
    path("pagos/", include("pagos.urls")),
    path("usuarios/", include("usuarios.urls")),
    path("registros/", include("registros.urls")),
    path("chatbot/", include("chatbot_app.urls")),
    path("gestion/", include("gestion_cabanas.urls")),
    path("interfaz/", include("interfaz_gestion_cabanas.urls")),
    path("web/", include("web.urls")),
]
