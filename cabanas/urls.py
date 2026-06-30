from django.contrib import admin
from django.urls import path
from . import handles

urlpatterns = [
    path("admin/", admin.site.urls),
    path("panel/", handles.panel_django, name="panel_django"),

    # Clientes
    path("clientes/", handles.cliente_list, name="cliente_list"),
    path("clientes/nuevo/", handles.cliente_create, name="cliente_create"),
    path("clientes/<int:pk>/editar/", handles.cliente_edit, name="cliente_edit"),
    path("clientes/<int:pk>/borrar/", handles.cliente_delete, name="cliente_delete"),

    # Reservas
    path("reservas/", handles.reserva_list, name="reserva_list"),
    path("reservas/nueva/", handles.reserva_create, name="reserva_create"),

    # Alquileres
    path("alquileres/", handles.alquiler_list, name="alquiler_list"),
    path("alquileres/nuevo/", handles.alquiler_create, name="alquiler_create"),

    # Pagos
    path("pagos/", handles.pago_list, name="pago_list"),
    path("pagos/nuevo/", handles.pago_create, name="pago_create"),

    # Registros
    path("registros/", handles.registro_list, name="registro_list"),
    path("registros/nuevo/", handles.registro_create, name="registro_create"),
]
