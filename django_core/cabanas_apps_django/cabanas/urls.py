"""URLs de la aplicación Cabañas, integradas con el sistema."""

from django.urls import include, path

from .views import (
    CabanaCreateView,
    CabanaDeleteView,
    CabanaDetailView,
    CabanaListView,
    CabanaUpdateView,
)

app_name = "cabanas"  # pylint: disable=invalid-name

urlpatterns = [
    # CRUD de cabañas
    path("", CabanaListView.as_view(), name="cabana_list"),
    path("nueva/", CabanaCreateView.as_view(), name="cabana_create"),
    path("<int:pk>/", CabanaDetailView.as_view(), name="cabana_detail"),
    path("<int:pk>/editar/", CabanaUpdateView.as_view(), name="cabana_update"),
    path("<int:pk>/borrar/", CabanaDeleteView.as_view(), name="cabana_delete"),
    # 🔗 Integraciones con otras apps del sistema
    path("alquileres/", include("cabanas_api.urls")),  # relación con alquileres
    path("reservas/", include("django_core.cabanas_apps_django.reservas.urls")),
    path("clientes/", include("django_core.cabanas_apps_django.clientes.urls")),
    path("pagos/", include("django_core.cabanas_apps_django.pagos.urls")),
    # usuarios eliminado porque la app ya no existe
]
