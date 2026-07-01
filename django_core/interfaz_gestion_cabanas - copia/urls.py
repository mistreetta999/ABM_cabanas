from django.urls import path
from . import handles

urlpatterns = [
    path("", handles.pagina_principal_html, name="pagina_principal"),
    path("gestion_cabanas/", handles.gestion_cabanas, name="gestion_cabanas"),
    path("panel/", handles.panel_django_gestion_cabanas, name="panel_django"),
    path("dashboard/", handles.dashboard, name="dashboard"),
    path("clientes/", handles.clientes, name="clientes"),
    path("reservas/", handles.reservas, name="reservas"),
    path("pagos/", handles.pagos, name="pagos"),
    path("cabanas/", handles.cabanas, name="cabanas"),
    path("chatbot/", handles.chatbot_home, name="chatbot_home"),
    path("chatbot/api/", handles.chatbot_api, name="chatbot_api"),


]
