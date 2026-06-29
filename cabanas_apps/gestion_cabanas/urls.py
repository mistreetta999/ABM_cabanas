"""URL patterns for the gestion_cabanas app."""
from django.urls import path
from . import reservas

urlpatterns = [
    path("reservas/", reservas.listar_reservas, name="listar_reservas"),
    path("reservas/<int:reserva_id>/", reservas.detalle_reserva, name="detalle_reserva"),
    path("reservas/nueva/<int:cliente_id>/<int:cabana_id>/", reservas.crear_reserva, name="crear_reserva"),
    path("reservas/borrar/<int:reserva_id>/", reservas.borrar_reserva, name="borrar_reserva"),
]
