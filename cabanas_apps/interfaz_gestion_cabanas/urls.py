""" archivo de urls para la app interfaz_gestion_cabanas """
from django.urls import path
from ...interfaz_gestion_cabanas import handles

urlpatterns = [
    path("", handles.pagina_principal_html, name="pagina_principal"),
    path("gestion_cabanas/", handles.gestion_cabanas, name="gestion_cabanas"),
    path("interfaz_gestion_cabanas/", handles.gestion_cabanas, name="gestion_cabanas"),
    path("panel/", handles.panel_django_gestion_cabanas, name="panel_django"),
    path("dashboard/", handles.dashboard, name="dashboard"),
    path("clientes/", handles.clientes, name="clientes"),
    path("reservas/", handles.reservas, name="reservas"),
    path("pagos/", handles.pagos, name="pagos"),
    path("cabanas/", handles.cabanas, name="cabanas"),
    path("chatbot/", handles.chatbot_home, name="chatbot_home"),
    path("chatbot/api/", handles.chatbot_api, name="chatbot_api"),
    path("alquileres/api/", handles.alquileres_api, name="alquileres_api"),


]
