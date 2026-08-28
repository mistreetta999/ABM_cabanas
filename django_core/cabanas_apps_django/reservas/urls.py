"""URLs de la aplicación Reservas, integradas con el sistema."""

from django.urls import path, include
from .views import (
    ReservaListView,
    ReservaCreateView,
    ReservaUpdateView,
    ReservaDeleteView,
    ReservaDetailView,
)

app_name = "reservas"

urlpatterns = [
    # CRUD de reservas
    path("", ReservaListView.as_view(), name="reserva_list"),
    path("nueva/", ReservaCreateView.as_view(), name="reserva_create"),
    path("<int:pk>/", ReservaDetailView.as_view(), name="reserva_detail"),
    path("<int:pk>/editar/", ReservaUpdateView.as_view(), name="reserva_update"),
    path("<int:pk>/borrar/", ReservaDeleteView.as_view(), name="reserva_delete"),

    # 🔗 Integraciones con otras apps del sistema
    path("cabanas/", include("cabanas.urls")),                # relación con cabañas
    path("alquileres/", include("alquileres.urls")),          # relación con alquileres
    path("clientes/", include("clientes.urls")),              # relación con clientes
    path("facturas/", include("facturas.urls")),              # relación con facturas
    path("pagos/", include("pagos.urls")),                    # relación con pagos
    path("usuarios/", include("usuarios.urls")),              # relación con usuarios
    path("chatbot/", include("chatbot_app.urls")),            # relación con chatbot
    path("gestion/", include("gestion_cabanas.urls")),        # relación con gestión de cabañas
    path("interfaz/", include("interfaz_gestion_cabanas.urls")),  # relación con interfaz de gestión
    path("registros/", include("registros.urls")),            # relación con registros
]
