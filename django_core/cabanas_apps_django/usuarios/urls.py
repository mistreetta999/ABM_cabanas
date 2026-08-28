"""URLs de la aplicación Usuarios, integradas con el sistema."""

from django.urls import path, include
from .views import (
    UsuarioListView,
    UsuarioCreateView,
    UsuarioUpdateView,
    UsuarioDeleteView,
    UsuarioDetailView,
)

app_name = "usuarios"

urlpatterns = [
    # CRUD de usuarios
    path("", UsuarioListView.as_view(), name="usuario_list"),
    path("nuevo/", UsuarioCreateView.as_view(), name="usuario_create"),
    path("<int:pk>/", UsuarioDetailView.as_view(), name="usuario_detail"),
    path("<int:pk>/editar/", UsuarioUpdateView.as_view(), name="usuario_update"),
    path("<int:pk>/borrar/", UsuarioDeleteView.as_view(), name="usuario_delete"),

    # 🔗 Integraciones con otras apps del sistema
    path("cabanas/", include("cabanas.urls")),                # relación con cabañas
    path("alquileres/", include("alquileres.urls")),          # relación con alquileres
    path("reservas/", include("reservas.urls")),              # relación con reservas
    path("clientes/", include("clientes.urls")),              # relación con clientes
    path("facturas/", include("facturas.urls")),              # relación con facturas
    path("pagos/", include("pagos.urls")),                    # relación con pagos
    path("chatbot/", include("chatbot_app.urls")),            # relación con chatbot
    path("gestion/", include("gestion_cabanas.urls")),        # relación con gestión de cabañas
    path("interfaz/", include("interfaz_gestion_cabanas.urls")),  # relación con interfaz de gestión
    path("registros/", include("registros.urls")),            # relación con registros
]
