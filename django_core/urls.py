""""este archivo contiene las urls de la app registros"""
from django.contrib import admin
from django.urls import include, path
from cabanas_api.views import pagina_principal
from . import handles


urlpatterns = [
    
    # Panel de administración
    path("admin/", admin.site.urls),

    # Home / panel principal
    path("", include("cabanas_apps.urls")),

    # Chatbot
    path("chatbot/", include("chatbot.urls")),
    #pagina principal
    path("pagina_principal/", pagina_principal, name="pagina_principal"),

    # Módulos internos
    path("gestion_cabanas/", include("cabanas_apps.gestion_cabanas.urls")),
    # App principal de Cabanas
    path("interfaz/", include("cabanas_apps.interfaz_gestion_cabanas.urls")),
    path("cabanas/", include("cabanas.urls")),
    path("clientes/", include("cabanas_apps.clientes.urls")),
    path("reservas/", include("cabanas_apps.reservas.urls")),
    path("alquileres/", include("cabanas_apps.alquileres.urls")),
    path("cabanas/", include("cabanas_apps.cabanas.urls")),
    path("registros/", include("cabanas_apps.registros.urls")),
    path("gestion/", include("cabanas_apps.gestion_cabanas.gestion_cabanas")),
    
    path("reservas/", include("cabanas_apps.reservas.urls")),
    path("alquileres/", include("cabanas_apps.alquileres.urls")),
    path("pagos/", include("cabanas_apps.pagos.urls")),
    path("registros/", include("cabanas_apps.registros.urls")),
    path("chatbot/", include("cabanas_apps.chatbot_app.urls")),
    path("template/", include("cabanas_apps.template_app.urls")),
    path("interfaz_gestion_cabanas/", include("cabanas_apps.interfaz_gestion_cabanas.urls")),
    path("gestion_cabanas/", include("cabanas_apps.gestion_cabanas.urls")),
    path("clientes/", include("cabanas_apps.clientes.urls")),
    path("pagina_principal/", include("cabanas_apps.pagina_principal.urls")),
    path("formulario/", include("cabanas_apps.formulario.urls")),
    
    path("admin/", admin.site.urls),
    path("", handles.pagina_principal, name="pagina_principal"),
    path("formularios/", handles.Formularios_panel_Django, name="formularios_panel"),
    path("imagenes/", handles.imagen_panel_Django, name="imagenes_panel"),
    path("cabanas/", handles.cabanas_panel_Django, name="cabanas_panel"),
    path("reservas/", handles.reservas_panel_Django, name="reservas_panel"),
    path("chatbot/", handles.chatbot_panel_Django   , name="chatbot_panel"),
    path("", handles.pagina_principal, name="pagina_principal"),
    path("gestion_cabanas/", handles.gestion_cabanas, name="gestion_cabanas"),
    path("panel/", handles.panel_django, name="panel_django"),
    path("dashboard/", handles.dashboard, name="dashboard"),
    path("clientes/", handles.clientes, name="clientes"),
    path("reservas/", handles.reservas, name="reservas"),
    path("pagos/", handles.pagos, name="pagos"),
    path("cabanas/", handles.cabanas, name="cabanas"),
    path("chatbot/", handles.chatbot_home, name="chatbot_home"),
    path("chatbot/api/", handles.chatbot_api, name="chatbot_api"),
    path("cabanas/", include("cabanas_apps.cabanas.urls")),

]
