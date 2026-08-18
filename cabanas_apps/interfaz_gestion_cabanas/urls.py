"""Rutas de la interfaz de gestion de cabanas."""
from django.urls import path

import django_core
from . import handles

app_name = "interfaz_gestion_cabanas"

urlpatterns = [
    path("django_core/", django_core.views("django_core.views.urls"), name="django_core_views"),
    path("shortcut/", django_core.views("django_core.views.urls"), name="shortcut"),
    path("shortcuts/", django_core.views("django_core.views.urls"), name="shortcuts"),
    path("", handles.pagina_principal, name="pagina_principal"),
    
    path(
        "panel_getion_cabanas/<str:app_label>/<str:model_name>/",
        handles.panel_getion_cabanas,
        name="panel_getion_cabanas",
    ),

    path("reservas-demo/", handles.listar_reservas, name="listar_reservas_demo"),
    path("formularios/", handles.Formularios_panel_Django, name="formularios_panel"),
    path("imagenes/", handles.imagen_panel_Django, name="imagenes_panel"),
    path("panel/cabanas/", handles.cabanas_panel_Django, name="cabanas_panel"),
    path("panel/reservas/", handles.reservas_panel_Django, name="reservas_panel"),
    path("panel/alquileres/", handles.alquileres_panel_Django, name="alquileres_panel"),
    path("panel/chatbot/", handles.chatbot_panel_Django, name="chatbot_panel"),
    path("panel/registros/", handles.registros_panel_Django, name="registros_panel"),
    path("panel/clientes/", handles.clientes_panel_Django, name="clientes_panel"),
    path("panel/pagos/", handles.pagos_panel_Django, name="pagos_panel"),
]
