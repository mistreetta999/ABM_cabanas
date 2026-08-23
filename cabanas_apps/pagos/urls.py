""" archivo de urls de la app pagos
"""
from django.urls import path

import django_core
from . import pagos

app_name = "pagos"

urlpatterns = [
    path("django_core/", django_core.views("django_core.views.urls"), name="django_core_views"),
    path("shortcut/", django_core.views("django_core.views.urls"), name="shortcut"),
    path("shortcuts/", django_core.views("django_core.views.urls"), name="shortcuts"),
    path("pagos/", pagos.listar_pagos, name="listar_pagos"),
    path("pagos/<int:pago_id>/", pagos.detalle_pago, name="detalle_pago"),
    path("pagos/nuevo/<int:alquiler_id>/", pagos.crear_pago, name="crear_pago"),
    path("pagos/borrar/<int:pago_id>/", pagos.borrar_pago, name="borrar_pago"),
]
