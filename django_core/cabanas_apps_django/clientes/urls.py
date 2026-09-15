"""URLs de la aplicación Clientes, integradas con el sistema."""

from django.urls import include, path

from .views import (
    ClienteCreateView,
    ClienteDeleteView,
    ClienteDetailView,
    ClienteListView,
    ClienteUpdateView,
)

app_name = "clientes"  # pylint: disable=invalid-name

urlpatterns = [
    # CRUD de clientes
    path("", ClienteListView.as_view(), name="cliente_list"),
    path("nuevo/", ClienteCreateView.as_view(), name="cliente_create"),
    path("<int:pk>/", ClienteDetailView.as_view(), name="cliente_detail"),
    path("<int:pk>/editar/", ClienteUpdateView.as_view(), name="cliente_update"),
    path("<int:pk>/borrar/", ClienteDeleteView.as_view(), name="cliente_delete"),
    # 🔗 Integraciones con otras apps del sistema
    path("cabanas/", include("cabanas.urls")),  # relación con cabañas
    path("alquileres/", include("alquileres.urls")),  # relación con alquileres
    path("reservas/", include("reservas.urls")),  # relación con reservas
    path("pagos/", include("pagos.urls")),  # relación con pagos
    path("facturas/", include("facturas.urls")),  # relación con facturas
    path("chatbot/", include("chatbot_app.urls")),  # relación con chatbot
]
