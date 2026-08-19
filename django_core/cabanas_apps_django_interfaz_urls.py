from django.urls import path
from .views import Cabana,Cliente

app_name = "interfaz_gestion_cabanas"

urlpatterns = [
    # Página principal de la interfaz
    path("", views.index, name="index"),

    # Gestión de cabañas
    path("cabanas/", views.lista_cabanas, name="lista_cabanas"),
    path("cabanas/<int:cabana_id>/", views.detalle_cabana, name="detalle_cabana"),

    # Gestión de reservas
    path("reservas/", views.lista_reservas, name="lista_reservas"),
    path("reservas/<int:reserva_id>/", views.detalle_reserva, name="detalle_reserva"),

    # Gestión de clientes
    path("clientes/", views.lista_clientes, name="lista_clientes"),
    path("clientes/<int:cliente_id>/", views.detalle_cliente, name="detalle_cliente"),

    # Gestión de pagos
    path("pagos/", views.lista_pagos, name="lista_pagos"),
    path("pagos/<int:pago_id>/", views.detalle_pago, name="detalle_pago"),
]
