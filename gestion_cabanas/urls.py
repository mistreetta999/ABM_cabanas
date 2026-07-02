"""URL patterns for the gestion_cabanas app."""
from django.urls import path
from . import reservas


urlpatterns = [
    path("reservas/", reservas.listar_reservas, name="listar_reservas"),
    path("", views.pagina_principal, name="pagina_principal"),
    path(
        "reservas/<int:reserva_id>/",
        reservas.detalle_reserva,
        name="detalle_reserva",
    ),
    path(
        "reservas/nueva/<int:cliente_id>/<int:cabana_id>/",
        reservas.crear_reserva,
        name="crear_reserva",
    ),
    path(
        "reservas/borrar/<int:reserva_id>/",
        reservas.borrar_reserva,
        name="borrar_reserva",
    ),
   path("alquileres/", reservas.listar_reservas, name="listar_reservas"),
    path("", views.pagina_principal, name="pagina_principal"),
    path(
        "alquileres/<int:reserva_id>/",
        reservas.detalle_reserva,
        name="detalle_reserva",
    ),
    path(
        "alquileres/nueva/<int:cliente_id>/<int:cabana_id>/",
        reservas.crear_reserva,
        name="crear_reserva",
    ),
    path(
        "alquileres/borrar/<int:reserva_id>/",
        reservas.borrar_reserva,
        name="borrar_reserva",
    ),



   path("pagos/", reservas.listar_reservas, name="listar_reservas"),
    path("", views.pagina_principal, name="pagina_principal"),
    path(
        "pagos/<int:reserva_id>/",
        reservas.detalle_reserva,
        name="detalle_reserva",
    ),
    path(
        "pagos/nueva/<int:cliente_id>/<int:cabana_id>/",
        reservas.crear_reserva,
        name="crear_reserva",
    ),
    path(
        "pagos/borrar/<int:reserva_id>/",
        reservas.borrar_reserva,
        name="borrar_reserva",
    ),



]
