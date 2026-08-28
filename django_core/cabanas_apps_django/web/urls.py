"""URLs de la aplicación Web, integradas con el sistema."""

from django.urls import path, include
from .views import (
    WebHomeView,
    WebAboutView,
    WebContactView,
)

app_name = "web"

urlpatterns = [
    # Páginas principales del sitio web
    path("", WebHomeView.as_view(), name="web_home"),
    path("about/", WebAboutView.as_view(), name="web_about"),
    path("contacto/", WebContactView.as_view(), name="web_contact"),

    # 🔗 Integraciones con otras apps del sistema
    path("cabanas/", include("cabanas.urls")),                # relación con cabañas
    path("alquileres/", include("alquileres.urls")),          # relación con alquileres
    path("reservas/", include("reservas.urls")),              # relación con reservas
    path("clientes/", include("clientes.urls")),              # relación con clientes
    path("facturas/", include("facturas.urls")),              # relación con facturas
    path("pagos/", include("pagos.urls")),                    # relación con pagos
    path("usuarios/", include("usuarios.urls")),              # relación con usuarios
    path("chatbot/", include("chatbot_app.urls")),            # relación con chatbot
    path("gestion/", include("gestion_cabanas.urls")),        # relación con gestión de cabañas
    path("interfaz/", include("interfaz_gestion_cabanas.urls")),  # relación con interfaz de gestión
    path("registros/", include("registros.urls")),            # relación con registros
]
