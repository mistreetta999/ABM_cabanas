"""URLs de la aplicación Gestión de Cabañas, integradas con el sistema."""

from django.urls import path, include
from .views import (
    GestionHomeView,
    CabanaGestionListView,
    CabanaGestionDetailView,
    CabanaGestionUpdateView,
)

app_name = "gestion_cabanas"

urlpatterns = [
    # Vistas principales de gestión
    path("", GestionHomeView.as_view(), name="gestion_home"),
    path("cabanas/", CabanaGestionListView.as_view(), name="cabana_list"),
    path("cabanas/<int:pk>/", CabanaGestionDetailView.as_view(), name="cabana_detail"),
    path("cabanas/<int:pk>/editar/", CabanaGestionUpdateView.as_view(), name="cabana_update"),

    # 🔗 Integraciones con otras apps del sistema
    path("cabanas/", include("cabanas.urls")),                # relación con cabañas
    path("alquileres/", include("alquileres.urls")),          # relación con alquileres
    path("reservas/", include("reservas.urls")),              # relación con reservas
    path("clientes/", include("clientes.urls")),              # relación con clientes
    path("facturas/", include("facturas.urls")),              # relación con facturas
    path("pagos/", include("pagos.urls")),                    # relación con pagos
    path("usuarios/", include("usuarios.urls")),              # relación con usuarios
    path("chatbot/", include("chatbot_app.urls")),            # relación con chatbot
    path("interfaz/", include("interfaz_gestion_cabanas.urls")),  # relación con interfaz de gestión
    path("registros/", include("registros.urls")),            # relación con registros
    path("web/", include("web.urls")),                        # relación con web pública
]
