""" archivo de urls de la app pagos
"""
from django.urls import path
from . import pagos

urlpatterns = [
    path("pagos/", pagos.listar_pagos, name="listar_pagos"),
    path("pagos/<int:pago_id>/", pagos.detalle_pago, name="detalle_pago"),
    path("pagos/nuevo/<int:alquiler_id>/", pagos.crear_pago, name="crear_pago"),
    path("pagos/borrar/<int:pago_id>/", pagos.borrar_pago, name="borrar_pago"),
]
