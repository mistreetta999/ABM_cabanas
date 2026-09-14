"""URLs para la aplicación Registros."""
from django.urls import path
from django_core.cabanas_apps_django.reservas.views import ListaReservasView
from django_core.cabanas_apps_django.reservas.views import DetalleReservaView
from django_core.cabanas_apps_django.reservas.views import CrearReservaView
from django_core.cabanas_apps_django.reservas.views import EditarReservaView
from django_core.cabanas_apps_django.reservas.views import EliminarReservaView


urlpatterns = [
    path("lista/", ListaReservasView.as_view(), name="lista_reservas"),
    path("detalle/<int:pk>/", DetalleReservaView.as_view(), name="detalle_reserva"),
    path("crear/", CrearReservaView.as_view(), name="crear_reserva"),
    path("editar/<int:pk>/", EditarReservaView.as_view(), name="editar_reserva"),
    path("eliminar/<int:pk>/", EliminarReservaView.as_view(), name="eliminar_reserva"),
]
