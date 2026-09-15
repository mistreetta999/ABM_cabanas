"""URLs de la aplicación de reservas."""

from django.urls import path

from .views import (
    CrearReservaView,
    DetalleReservaView,
    EditarReservaView,
    EliminarReservaView,
    ListaReservasView,
)

urlpatterns = [
    path("lista/", ListaReservasView.as_view(), name="lista_reservas"),
    path("detalle/<int:pk>/", DetalleReservaView.as_view(), name="detalle_reserva"),
    path("crear/", CrearReservaView.as_view(), name="crear_reserva"),
    path("editar/<int:pk>/", EditarReservaView.as_view(), name="editar_reserva"),
    path("eliminar/<int:pk>/", EliminarReservaView.as_view(), name="eliminar_reserva"),
]
